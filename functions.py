import random

VOWELS_LIST = ['a', 'e', 'i', 'o', 'u']
NUMBERS_LIST = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SPECIAL_CHARACTERS_LIST = [';', ':', '@', ',']
CONSONANTS_LIST = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y',
                   'z']

MOVIE_NAME = ['war', 'happy bhag jayegi', 'spider man']


def string_parse(*args, random_movie_name=True, ) -> str:
    """
    returns a string without values selected in args
    :param random_movie_name: default True 
    :param args: first argument to be string,0 -> vowels, 1 -> consonants, 2 -> numbers, 3 -> special characters
    :return: string
    """

    # Setting string
    if random_movie_name:
        string = random_name()
    else:
        string = args[0].lower()

    list_of_variables_to_be_excluded = []
    string_to_be_returned = ""
    for i in args:
        if i == 0:
            for k in VOWELS_LIST:
                list_of_variables_to_be_excluded.append(k)
        if i == 1:
            for k in CONSONANTS_LIST:
                list_of_variables_to_be_excluded.append(k)
        if i == 2:
            for k in NUMBERS_LIST:
                list_of_variables_to_be_excluded.append(k)
        if i == 3:
            for k in SPECIAL_CHARACTERS_LIST:
                list_of_variables_to_be_excluded.append(k)

    for i in string:
        for j in list_of_variables_to_be_excluded:
            if i == j:
                string_to_be_returned += "_"
                break
        else:
            string_to_be_returned += i
    return string_to_be_returned, string


def random_name() -> str:
    """
    Choses a random movie name
    :return: Random movie name
    """
    choice = random.randint(0, len(MOVIE_NAME) - 1)
    return MOVIE_NAME[choice]
