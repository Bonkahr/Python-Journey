class Song:
    """ Class to represent a song

    Attributes:
        title (str): The song title.
        artist (str): Name of the song creator.
        duration (int): The duration of the song in seconds. May be zero.
    """

    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """ Class to represent an album, using its track list

    Attributes:
        name (str): The name of the album
        year (int): The release year
        artist (str): Name of the artist
        tracks (str): List of songs in the album

    Methods:
        add_song: Used to add a new song to the album track list

    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = 'Various Artists'
        else:
            self.artist = artist

        self.tracks = []

    def add_song(self, song, position=None):
        """ Add a song to track list

        Args:
            song(Song): A title of song to add
            position(optional[int]): Song will be added at the specified
            position if provided
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Basic class to store Artist details

    Attributes:
        name (str): Then name of the artist
        albums (list[album]): A list of albums by the artist

    Methods:
        add_album: Used to add album to the artist album list
    """

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        """
        Add new album to the list

        :param album: Album object to add to list
        """
        self.albums.append(album)

    def add_song(self, name, year, title):
        """
        Add a new song to the collection of albums
        this method will add the song to an album in collection
        A new album will be created in the collection if it doesnt already
        exist.
        :param name: The name of the album
        :param year: The year of the Album
        :param title: The title of the song
        :return:
        """

        album_found = find_object(name, self.albums)
        if album_found is None:
            print(f'{name}, not found')
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print(f'Found album, {name}')
        album_found.add_song(title)


def find_object(field, obj_list):
    """
    check 'object_list' to see if an object with 'name' attribute equal to
    'field' exists, return it if so
    """

    for item in obj_list:
        if item.name == field:
            return item
    return None


def load_data():
    # new_artist = None
    # new_album = None
    artist_list = []

    with open('albums.txt', 'r') as albums:
        for line in albums:
            # data row should consist of (artist, album, year, song)
            artist_field, album_field, year_field, song_field = \
                tuple(line.strip('\n').split('\t'))
            print(f'{artist_field}:{album_field}:{year_field}:{song_field}')

            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            new_artist.add_song(album_field, year_field, song_field)

    return artist_list


def create_check_file(artist_list):
    """ Create a check file from the object data for comparison with the
    original file
    """
    with open('check_file.txt', 'w') as check_file:
        for new_artist in artist_list:
            for new_album in new_artist.albums:
                for new_song in new_album.tracks:
                    print(f'{new_artist.name}\t{new_album.name}\t'
                          f'{new_album.year}\t{new_song.title}',
                          file=check_file)


if __name__ == '__main__':
    artists = load_data()
    print(f'There are {len(artists)} artists in the list.')

    create_check_file(artists)
