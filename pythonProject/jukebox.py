from my_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please choose your album (invalid choice exists): ")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}"
              .format(index + 1, title))

    choice = int(input("Enter your choice: "))
    if 1 <= choice <= len(albums):
        songs_list = albums[choice-1][SONGS_LIST_INDEX]
    #   print("song list: {} ".format(songs_list))
    else:
        break

    print("please choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))

    songs_choice = int(input())
    if 1 <= songs_choice <= len(songs_list):
        title = songs_list[songs_choice - 1][SONG_TITLE_INDEX]
        print("playing: {}".format(title))
        print("=" * 40)
