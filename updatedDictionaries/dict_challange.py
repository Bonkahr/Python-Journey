from contents import recipes


def my_deepcopy(d: dict) -> dict:
    """
    copy a dictionary , creating copies of the `list` or `dict` values
    The function will crash on attribute error if the values aren't lists or
    dict
    :param d: The dictionary to copy
    :return: A copy of `d`, with the values being copied
    """
    new_dict = {}
    for key, values in d.items():
        new_value = values.copy()
        new_dict[key] = new_value
    return new_dict


if __name__ == '__main__':
    recipe_copy = my_deepcopy(recipes)
    recipe_copy['Butter chicken']['ginger'] = 30
    print(recipe_copy['Butter chicken']['ginger'])
    print(recipes['Butter chicken']['ginger'])
