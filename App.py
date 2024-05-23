import streamlit as st
from pytube import YouTube
from YoutubeDL import youtubeDL

st.title('Youtube ダウンロード')

with st.form(key="name-form"):
 inputText = st.text_input("youtubeリンク", key="link")
 submit_button = st.form_submit_button(label="探す")

 if submit_button and inputText:
    downloader = youtubeDL()
    yt = downloader.checkYoutube(inputText)
    if yt:
     st.write(f"動画のタイトル: {yt['title']}")
     st.image(yt['thumbnail_url']) 
    else:
      st.write("動画が見つかりません。")  
 

