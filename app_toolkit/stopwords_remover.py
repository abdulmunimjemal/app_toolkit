"""
*************************************************************************
* Function: A python program to remove amharic stopwords from a list. . *
* Usage: import remove_stopwords(list)                                  *
* Author: Abdulmunim J Jemal                                            *
* Prepared as part of the Amharic Spell Checker Project                 *
* Course: Fundamentals of Software Engineering                          *
* Department/Campus:  Software Engineering/AAiT                         *
* Date:  27/10/2023 G.C                                                 *
*************************************************************************
"""

DEFAULT_PATH = "data/stopwords-am.txt"


def remove_stopwords(input_list: list, stopwords_file: str = DEFAULT_PATH) -> list:
    """
    Removes stopwords from a list
    """
    if type(input_list) == str:
        input_list = input_list.split(' ')

    STOPWORDS_LIST = []
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        STOPWORDS_LIST = [line.rstrip() for line in file.readlines()]

    output_list = []
    for line in input_list:
        line = line.strip()  # remove leading and trailing whitespaces
        if line not in STOPWORDS_LIST:
            output_list.append(line)
    return output_list


def help():
    """
    Shows how to use the module
    """
    print("***********************************************")
    print("WARNING: You can not run this module directly.\n\tPlease import it instead.")
    print("***********************************************")


if __name__ == '__main__':
    help()
