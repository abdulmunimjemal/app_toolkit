"""
*************************************************************************
* Function: Transliterate Amharic Geez terms to Latin Alphabet          *
* Author: Abdulmunim J Jemal                                            *
* Prepared as part of the Amharic Spell Checker Project                 *
* Course: Fundamentals of Software Engineering                          *
* Department/Campus:  Software Engineering/AAiT                         *
* Date:  28/10/2023 G.C                                                 *
*************************************************************************
"""

from collections import defaultdict

DEFAULT_PATH = "data/transliteration.txt"
lookup_table = defaultdict(lambda: "X")

with open(DEFAULT_PATH, 'r', encoding='utf-8') as file:
    for line in file.readlines():
        line = line.rstrip()
        if line:
            key, value = line.split(':')
            lookup_table[key] = value

vowels = "aeiou"


def transliterate(word: str, lang: str = "am") -> str:
    """
    Transliterates between Amharic and English.
    Args:
        word (str): The word to be transliterated.
        lang (str, optional): The language of the word. Defaults to "am" (Amharic).

    Returns:
        str: The transliterated word.

    Usage:
    To transliterate an Amharic word to English:
    >>> word = "ወንበር"
    >>> transliterate(word, "am")
    "wenber"

    To transliterate an English word to Amharic:
    >>> word = "leba"
    >>> transliterate(word, "en")
    "ለባ"
    """

    if lang not in ["am", "en"]:
        raise ValueError(
            "Invalid language. Use 'am' for Amharic or 'en' for English.")

    transliterated_word = ""

    if lang == "am":  # transiliterate from amharic to english
        tokens = list(word)
        for letter in tokens:
            transliterated_word += lookup_table[letter]
    elif lang == "en":  # transiliterate from english to amharic
        tokens = [word[i:i + 2]
                  for i in range(0, len(word), 2)]  # two characters
        if len(tokens) == 0:
            return transliterated_word

        for letter in tokens:  # iterate through each english pair
            if letter[0] not in vowels and letter[1] in vowels:
                am_letter = ""
                if letter == "Wa":  # handling a special case Wa
                    for key, value in lookup_table.items():
                        if value == letter.lower():
                            am_letter = key
                            break
                else:
                    am_letter = next(
                        (key for key, value in lookup_table.items() if value == letter.lower()), None)
                if am_letter is not None:
                    transliterated_word += am_letter
            else:
                ltrs = list(letter)  # split into individual letters
                for ltr in ltrs:
                    am_letter = next(
                        (key for key, value in lookup_table.items() if value == ltr.lower()), None)
                    if am_letter is not None and am_letter != "ኧ":
                        transliterated_word += am_letter
    return transliterated_word


if __name__ == "__main__":
    print(transliterate.__doc__)
