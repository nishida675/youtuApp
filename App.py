import streamlit as st
import os
import tempfile
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

# 保存先が選択されている場合にダウンロードボタンを表示
if st.session_state['yt_info'] and st.session_state['download_option']:
    if st.button("ダウンロード"):
        yt = st.session_state['yt_info']['yt_object']
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            if st.session_state['download_option'] == "動画":
                # 最初の動画ストリームをダウンロード
                video_stream = yt.streams.filter(file_extension='mp4').first()
                tmp_file_path = video_stream.download(output_path=os.path.dirname(tmp_file.name), filename=os.path.basename(tmp_file.name))
                st.session_state['download_path'] = tmp_file_path
                st.success("動画のダウンロードが完了しました。")
            elif st.session_state['download_option'] == "オーディオ":
                # 最初のオーディオストリームをダウンロード
                audio_stream = yt.streams.filter(only_audio=True).first()
                tmp_file_path = audio_stream.download(output_path=os.path.dirname(tmp_file.name), filename=os.path.basename(tmp_file.name))
                st.session_state['download_path'] = tmp_file_path
                st.success("オーディオのダウンロードが完了しました。")
        
        # ダウンロードリンクを提供
        with open(st.session_state['download_path'], 'rb') as file:
            st.download_button(
                label="ファイルをダウンロード",
                data=file,
                file_name=os.path.basename(st.session_state['download_path']),
                mime='application/octet-stream'
            )
