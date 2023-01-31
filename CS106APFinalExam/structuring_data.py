def get_genre_data(filenames: str) -> dict:
    """
    Returns a dictionary containing article data, where the genre
    is the key and a list of tuples containing article information
    is the value. Takes in a list of filenames, where each file
    corresponds to the article data for a single genre.
    Input:
    filenames (list of strings): list of files containing genre
    data
    Returns:
    genre_data (dict: string -> list of tuples): dict of articles
    organized by
    genre
    """
    file_key = filenames.split('\n')[0]
    # list_tuple_lines = [x.strip() for y in filenames.split('\n')[1:] for x in
    #                     y.split(',') if y]
    list_tuple_lines = [z.strip() for x in filenames.split('\n')[1:]
                        for z in x.split(',')]

    genre_dict = {file_key: [x for x in list_tuple_lines]}

    return genre_dict


if __name__ == '__main__':
    strings = ' Opinions\n\
    Why CS106AP is the Best Class,Kylie Jue,159\n\
    My Love Affair with Python,Sonja Johnson-Yu,106'

    print(get_genre_data(strings))
