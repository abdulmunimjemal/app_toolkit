"""
*************************************************************************
* Function: Eemove amharic stopwords from a list                        *
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
    Removes Amharic stopwords from a list of words.

    Args:
        input_list (list): The list of words from which stopwords should be removed.
        stopwords_file (str, optional): The path to the file containing Amharic stopwords. Defaults to DEFAULT_PATH.

    Returns:
        list: The list of words with stopwords removed.

    Example:
    >>> word_list = ["ለዚህ", "ቅሬታ", "ምን", "ነህ"]
    >>> stopwords_file = "data/stopwords.txt"  # Provide the path to your stopwords file
    >>> filtered_list = remove_stopwords(word_list, stopwords_file)
    >>> print(filtered_list)
    ['ለዚህ', 'ቅሬታ', 'ነህ']
    """

    if type(input_list) == str:
        input_list = input_list.split(' ')

    STOPWORDS_LIST = []
    with open(stopwords_file, 'r', encoding='utf-8') as file:
        STOPWORDS_LIST = [line.rstrip() for line in file.readlines()]

    filtered_list = []
    for line in input_list:
        line = line.strip()  # remove leading and trailing whitespaces
        if line not in STOPWORDS_LIST:
            filtered_list.append(line)
    return filtered_list


def help():
    """
    Shows how to use the module
    """
    print("***********************************************")
    print("WARNING: You can not run this module directly.\n\tPlease import it instead.")
    print("***********************************************")
    print(remove_stopwords.__doc__)


if __name__ == '__main__':
    help()
