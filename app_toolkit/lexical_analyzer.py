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
import argparse


DEFAULT_PATH = "data/abbreviations.txt"


abbreviations = defaultdict(lambda: None)
with open(DEFAULT_PATH, "r", encoding="utf-8") as f:
    for line in f:
        key, value = line.split(":")
        abbreviations[key.strip()] = value.strip()


def lexical_analyze(corpus: str, abbr: bool = True, punc: bool = True, numbers: bool = True) -> str:
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
    if abbr:
        for key, value in abbreviations.items():
            regex = re.compile(re.escape(key))
            corpus = regex.sub(value, corpus)

    if punc:
        corpus = re.sub(r"[.\?\"',/#!$%^&*;:፤።{}=\-_\`~()]", " ", corpus)
    if numbers:
        corpus = re.sub(r"[.፩፪፫፬፭፮፮፰፱፲፳፴፵፵፷፸፹፺፻0123456789]", " ", corpus)
        corpus = re.sub(r"\s{2,}", " ", corpus)

    return corpus


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Lexical analyzer for Amharic text document"
    )
    parser.add_argument("input_txt", type=str, help="Input text path")
    parser.add_argument("output_txt", type=str, help="Output text path")
    args = parser.parse_args()
    corpus = ""
    with open(args.input_txt, "r", encoding="utf-8") as f:
        corpus = f.read()
    output_text = lexical_analyze(corpus, abbr=False, punc=False)
    with open(args.output_txt, "w", encoding="utf-8") as f:
        f.write(output_text)
    print("Lexical analysis completed successfully!")
