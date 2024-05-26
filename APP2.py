import streamlit as st
import os
import tempfile
from pytube import YouTube
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

    submit_button = st.button('ダウンロード')
    if submit_button:
       video_url = 'https://www.youtube.com/watch?v=kj8kpQhiZpM'
       yt = YouTube(video_url)
       audio_streams = yt.streams.filter(only_audio=True)
       audio_stream = audio_streams.first()
       audio_stream.download() 