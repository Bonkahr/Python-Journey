import pickle
poem = ('More Mayhem',
        'Imelda May',
        '2011',
        ((1, 'Pulling the rug'),
         (2, 'Psycho'),
         (3, 'Mayhem'),
         (4, 'Knish Town Waltz')))
#
# with open("poem.pickle", 'wb') as pickle_file:
#     pickle.dump(poem, pickle_file)
with open('poem.pickle', 'rb') as poem_pickled:
    poem1 = pickle.load(poem_pickled)

print(poem1)

album, artist, year, track_list = poem1

print(album)
print(artist)
print(year)

for track in track_list:
    track_number, track_title = track
    print(track_number, track_title)
