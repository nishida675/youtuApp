import streamlit as st
from pytube import YouTube
import os

from YoutubeDL import youtubeDL  # 別ファイルからクラスをインポート

st.title('Youtube ダウンロード')

# セッションステートを使用してダウンロードオプションを保存
if 'yt_info' not in st.session_state:
    st.session_state['yt_info'] = None
if 'download_option' not in st.session_state:
    st.session_state['download_option'] = None
if 'download_path' not in st.session_state:
    st.session_state['download_path'] = None

# フォームの定義
with st.form(key="name-form"):
    input_text = st.text_input("youtubeリンク", key="link")
    submit_button = st.form_submit_button(label="探す")

# 動画情報の表示とダウンロードオプションの選択
if submit_button and input_text:
    downloader = youtubeDL()
    yt_info = downloader.checkYoutube(input_text)
    if yt_info:
        st.session_state['yt_info'] = yt_info
        st.session_state['download_option'] = None  # Reset download option on new search
    else:
        st.error("指定された動画は利用できません。")

# 動画情報の表示
if st.session_state['yt_info']:
    yt_info = st.session_state['yt_info']
    st.write(f"動画のタイトル: {yt_info['title']}")
    st.image(yt_info['thumbnail_url'])

    # ダウンロードオプションを選択
    st.session_state['download_option'] = st.radio(
        "ダウンロードオプションを選択してください",
        ("動画", "オーディオ")
    )

# ユーザーのダウンロードフォルダのパスを取得
if os.name == 'nt':  # Windowsの場合
    default_download_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')
else:  # MacやLinuxの場合
    default_download_path = os.path.join(os.path.expanduser('~'), 'Downloads')

st.session_state['download_path'] = default_download_path

# 保存先が選択されている場合にダウンロードボタンを表示
if st.session_state['yt_info'] and st.session_state['download_option']:
    if st.button("ダウンロード"):
        yt = st.session_state['yt_info']['yt_object']
        download_path = st.session_state['download_path']
        if st.session_state['download_option'] == "動画":
            # 最初の動画ストリームをダウンロード
            video_stream = yt.streams.filter(file_extension='mp4').first()
            download_path = video_stream.download(output_path=st.session_state['download_path'])
            st.session_state['download_path'] = download_path
            st.success("動画のダウンロードが完了しました。")
        elif st.session_state['download_option'] == "オーディオ":
            # 最初のオーディオストリームをダウンロード
            audio_stream = yt.streams.filter(only_audio=True).first()
            download_path = audio_stream.download(output_path=st.session_state['download_path'])
            st.session_state['download_path'] = download_path
            st.success("オーディオのダウンロードが完了しました。")

