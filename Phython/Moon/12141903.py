from pytube import YouTube
##유투브 해당 url 다운로드 ##
yt = YouTube("https://www.youtube.com/watch?v=BahhILeIkJ4")  #다운받으려는 url입력
yt.streams.first().download()
# print(yt.views)
# print(yt.vid_descr)

# for e in yt.streams.filter(file_extension='mp4').all():
#     print(str(e))