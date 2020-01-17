from pytube import Playlist

##유투브 플레이리스트 전체 다운로드##
pl = Playlist("https://www.youtube.com/playlist?list=PLymRkSJhEzqJ_mF5UGtZoYP_9xvcAncIf")
pl.download_all()