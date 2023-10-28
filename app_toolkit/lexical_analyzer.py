"""
*************************************************************************
* Function: Amharic Text Lexical Analyzer                               *
* Author: Abdulmunim J Jemal                                            *
* Prepared as part of the Amharic Spell Checker Project                 *
* Course: Fundamentals of Software Engineering                          *
* Department/Campus:  Software Engineering/AAiT                         *
* Date:  30/10/2023 G.C                                                 *
*************************************************************************
"""

import re
from collections import defaultdict


DEFAULT_PATH = "data/abbreviations.txt"


abbreviations = defaultdict(lambda: None)
with open(DEFAULT_PATH, "r", encoding="utf-8") as f:
    for line in f:
        key, value = line.split(":")
        abbreviations[key.strip()] = value.strip()


def lexical_analyze(corpus: str) -> str:
    """
    Separates words, expands common Amharic abbreviations, removes numbers, breaks up hyphenated words, and removes punctuation.

    Args:
        corpus (str): Amharic text.

    Returns:
        str: Lexically analyzed Amharic text.

    Example:
        >>> lexAnalyze("ዓ.ዓ ዓም")
        'ዓመተ ዓለም ዓመተ ምህረት'
    """

    # Remove abbreviations
    for key, value in abbreviations.items():
        regex = re.compile(re.escape(key))
        corpus = regex.sub(value, corpus)

    corpus = re.sub(r"[.\?\"',/#!$%^&*;:፤።{}=\-_\`~()]", " ", corpus)
    corpus = re.sub(r"[.፩፪፫፬፭፮፮፰፱፲፳፴፵፵፷፸፹፺፻0123456789]", " ", corpus)
    corpus = re.sub(r"\s{2,}", " ", corpus)

    return corpus


if __name__ == "__main__":
    print(lexical_analyze("ዓ.ዓ ዓም"))
