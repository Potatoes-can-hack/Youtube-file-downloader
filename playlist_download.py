from pytube import Playlist

video_group = Playlist('https://www.youtube.com/playlist?list=PLu0W_9lII9agS67Uits0UnJyrYiXhDS6q')
print(f'Downloading: {video_group.title}')
for video in video_group.videos:
    video.streams.last().download