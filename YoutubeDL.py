from pytube import YouTube
from pytube.exceptions import VideoUnavailable

class youtubeDL:
    def checkYoutube(self, video_url):
      try:
       yt = YouTube(video_url)
       return {
                'title': yt.title,
                'thumbnail_url': yt.thumbnail_url,
                'yt_object': yt
            }
      except VideoUnavailable:
            print("指定された動画は利用できません。")
      except Exception as e:
            print(f"エラーが発生しました: {e}")
# ダウンロードしたい動画のURLを設定
#video_url = 'https://www.youtube.com/watch?v=kj8kpQhiZpM'

# YouTubeオブジェクトを作成
#yt = YouTube(video_url)

# オーディオストリームをフィルタリングして取得
#audio_streams = yt.streams.filter(only_audio=True)
#audio_streams = yt.streams.filter(file_extension='mp4').all()

# 最初のオーディオストリームを選択
#audio_stream = audio_streams.first()

# オーディオストリームをダウンロード
#audio_stream.download()

print("ダウンロードが完了しました。")
