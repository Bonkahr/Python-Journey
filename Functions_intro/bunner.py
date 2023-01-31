def banner_text(text: str = "", screen_width: int = 60) -> None:
    """
    Print a string centred, with ** either side.

    :param text: The string to print.
        An asterisk (*) will result in a row of asterisks.
        The default will print a blank line, with a ** border at
        the left and right edges.
    :param screen_width: The overall width to print within
        (including the 4 spaces for the ** either side).
    :raises ValueError: if the supplied string is too long to fit.
    """
    if len(text) > screen_width - 4:
        raise ValueError("String {} is larger than specified width{}"
                         .format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        # v = 0
        # text_length = screen_width - len(text)
        # n = int(text_length / 2)
        # if text_length % 2 != 0:
        #     v = n + 1
        centred_text = text.center(screen_width - 4)
        output_string = "**{}**".format(centred_text)
        print(output_string)


banner_text("*", 60)
banner_text("hau ni ho", 60)
banner_text(screen_width=60)
banner_text("hfdhvf vfhbvhffv fhvbfhbvfv", 60)
banner_text("hfgf dhhuhfv hbvfhvufjidjf vfbvhffh", 60)
banner_text("*", 60)
