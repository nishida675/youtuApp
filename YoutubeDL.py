from pytube import YouTube

# ダウンロードしたい動画のURLを設定
video_url = 'https://www.youtube.com/watch?v=kj8kpQhiZpM'

# YouTubeオブジェクトを作成
yt = YouTube(video_url)

# オーディオストリームをフィルタリングして取得
audio_streams = yt.streams.filter(only_audio=True)
#audio_streams = yt.streams.filter(file_extension='mp4').all()

# 最初のオーディオストリームを選択
audio_stream = audio_streams.first()

# オーディオストリームをダウンロード
audio_stream.download()

print("ダウンロードが完了しました。")
