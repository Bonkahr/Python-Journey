# YouTube Downloader
from pytube import YouTube

try:
    yt = YouTube(input('Enter link: '))
    videos = yt.streams.filter(only_audio=True)
    for i in enumerate(videos, 1):
        print(i)
    choice = input('Enter option from above: ')
    try:
        choice = int(choice)
    except ValueError:
        input('Enter a valid choice, an integer: ')

    try:
        download = videos[int(choice) - 1]
        print('Downloading....')
        download.download('/home/bgakingo/Music/youtube/')
        print('Download successful')
    except IndexError:
        print('Error downloading your file, Not in list')
except:
    print('URL not found.')
