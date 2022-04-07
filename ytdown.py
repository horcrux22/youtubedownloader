import time

from pytube import YouTube,Playlist
from utils import make_dir

FILE_EXT='mp4'

def playlist(arg):
    
    playlist_url =Playlist(arg.url)

    save_dir = make_dir(arg.dir)

    for arg.url in playlist_url:
        start = time.time()
        
        yt = YouTube(arg.url)
        print('now :',yt.title)
        yt.streams.filter(adaptive=True, file_extension=FILE_EXT).order_by('resolution').desc().first().download(save_dir)
        
        end = time.time()

        print('done',f"{end-start:.3f} sec")
    return
    
def not_playlist(arg):

    save_dir = make_dir(arg.dir)
    
    start = time.time()
    
    yt = YouTube(arg.url)
    print('now :',yt.title)
    yt.streams.filter(adaptive=True, file_extension=FILE_EXT).order_by('resolution').desc().first().download(save_dir)
    
    end = time.time()
    return print('done',f"{end-start:.3f} sec")

