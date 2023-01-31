def centre(*args) -> None:
    """
    centre text in a 80 characters display
    :param args: any data type
    :return: None
    """
    text = '-'.join([str(arg) for arg in args])
    left_margin = (80 - len(text)) // 2
    print(' ' * left_margin, text)


centre("spam and eggs")
centre('spam, spam, and eggs')
centre(12)
centre('spam, spam, spam and spam')
centre('first, second, 3, 4, spam')
