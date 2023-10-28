"""
*************************************************************************
* Function: Amharic Word Stemmer - Returns the Amharic root word        *
* Author: Abdulmunim J Jemal                                            *
* Prepared as part of the Amharic Spell Checker Project                 *
* Course: Fundamentals of Software Engineering                          *
* Department/Campus:  Software Engineering/AAiT                         *
* Date:  29/10/2023 G.C                                                 *
*************************************************************************
"""


from transliterate import transliterate
import re


def load_affixes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return [line.rstrip() for line in f.readlines()]


def remove_suffix(cv_string, suffix):
    regex = re.compile(re.escape(suffix) + "$", re.IGNORECASE)
    return re.sub(regex, "", cv_string)


def remove_prefix(cv_string, prefix):
    regex = re.compile("^" + re.escape(prefix), re.IGNORECASE)
    return re.sub(regex, "", cv_string)


def remove_infix(cv_string):
    if re.search(r".+([^aeiou])[aeiou]\1[aeiou].?", cv_string, re.IGNORECASE):
        return re.sub(r"\S\S[^aeiou][aeiou]", cv_string[0] + cv_string[1], cv_string, flags=re.IGNORECASE)
    elif re.match(r"^(.+)a\1$", cv_string, re.IGNORECASE):
        return re.sub(r"a.+", "", cv_string, flags=re.IGNORECASE)
    return cv_string


def replace_double_consonant_e(cv_string):
    ccv_match = re.search(
        r"[bcdfghjklmnpqrstvwxyz]{2}e", cv_string, re.IGNORECASE)
    if ccv_match:
        ccv = ccv_match.group(0)
        return re.sub(r"[bcdfghjklmnpqrstvwxyz]{2}e", ccv[0] + "X" + ccv[1], cv_string, flags=re.IGNORECASE)
    return cv_string


def stem(word):
    """
    Takes an Amharic word and returns the stem through affix-removal with longest match.

    Args:
        word (str): Word possibly containing one or more affix.

    Returns:
        str: The stem of the word passed.

    Example:
        >>> stem("ልጆቻቸውን")
        'ልጅ'
    """
    cv_string = transliterate(word, "am")  # Consonant-vowel string

    suffix_list = load_affixes("data/transliteration_suffix.txt")
    prefix_list = load_affixes("data/transliteration_prefix.txt")

    # Prepare suffix list
    suffixes = [transliterate(suffix, "am") for suffix in suffix_list]
    suffixes.append("Wa")  # Special case for ሯ

    # Prepare prefix list
    prefixes = [transliterate(prefix, "am") for prefix in prefix_list]

    # Remove suffixes
    for suffix in suffixes:
        if cv_string.endswith(suffix):
            cv_string = remove_suffix(cv_string, suffix)
            break

    # Remove prefixes
    for prefix in prefixes:
        if cv_string.startswith(prefix):
            cv_string = remove_prefix(cv_string, prefix)
            break

    # Remove infixes
    cv_string = remove_infix(cv_string)

    # Replace double consonant "e"
    cv_string = replace_double_consonant_e(cv_string)

    return transliterate(cv_string, "en")


if __name__ == "__main__":
    print(stem.__doc__)
