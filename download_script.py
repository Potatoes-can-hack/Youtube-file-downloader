from pytube import YouTube

video = YouTube('https://www.youtube.com/watch?v=K0_-f2Qp_HI&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl&index=17')
                 
stream = video.streams.get_by_itag(22)
stream.download()

