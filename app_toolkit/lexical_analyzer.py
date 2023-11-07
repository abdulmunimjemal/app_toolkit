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
from .stopwords_remover import remove_stopwords
import argparse


# Abbreviaitions
DEFAULT_PATH = "data/abbreviations.txt"

abbreviations = defaultdict(lambda: None)
with open(DEFAULT_PATH, "r", encoding="utf-8") as f:
    for line in f:
        key, value = line.split(":")
        abbreviations[key.strip()] = value.strip()

# Character Level Normalization


def normalize_char_level(corpus):
    """
    A helper function for the lexical analyzer, helping with character level normalization
    """
    char_map = {
        'ሃኅኃሐሓኻ': 'ሀ',
        'ሑኁዅ': 'ሁ',
        'ኂሒኺ': 'ሂ',
        'ኌሔዄ': 'ሄ',
        'ሕኅ': 'ህ',
        'ኆሖኾ': 'ሆ',
        'ሠ': 'ሰ',
        'ሡ': 'ሱ',
        'ሢ': 'ሲ',
        'ሣ': 'ሳ',
        'ሤ': 'ሴ',
        'ሥ': 'ስ',
        'ሦ': 'ሶ',
        'ዓኣዐ': 'አ',
        'ዑ': 'ኡ',
        'ዒ': 'ኢ',
        'ዔ': 'ኤ',
        'ዕ': 'እ',
        'ዖ': 'ኦ',
        'ጸ': 'ፀ',
        'ጹ': 'ፁ',
        'ጺ': 'ፂ',
        'ጻ': 'ፃ',
        'ጼ': 'ፄ',
        'ጽ': 'ፅ',
        'ጾ': 'ፆ',
        'ሉ[ዋአ]': 'ሏ',
        'ሙ[ዋአ]': 'ሟ',
        'ቱ[ዋአ]': 'ቷ',
        'ሩ[ዋአ]': 'ሯ',
        'ሱ[ዋአ]': 'ሷ',
        'ሹ[ዋአ]': 'ሿ',
        'ቁ[ዋአ]': 'ቋ',
        'ቡ[ዋአ]': 'ቧ',
        'ቹ[ዋአ]': 'ቿ',
        'ሁ[ዋአ]': 'ኋ',
        'ኑ[ዋአ]': 'ኗ',
        'ኙ[ዋአ]': 'ኟ',
        'ኩ[ዋአ]': 'ኳ',
        'ዙ[ዋአ]': 'ዟ',
        'ጉ[ዋአ]': 'ጓ',
        'ደ[ዋአ]': 'ዷ',
        'ጡ[ዋአ]': 'ጧ',
        'ጩ[ዋአ]': 'ጯ',
        'ጹ[ዋአ]': 'ጿ',
        'ፉ[ዋአ]': 'ፏ',
        '[ቊ]': 'ቁ',  # ቁ can be written as ቊ
        '[ኵ]': 'ኩ',  # ኩ can be also written as ኵ
    }

    for pattern, replacement in char_map.items():
        corpus = re.sub(pattern, replacement, corpus)

    return corpus


def lexical_analyze(corpus: str, abbr: bool = True, punc: bool = True, numbers: bool = True, normalization: bool = True, stopwords: bool = False) -> str:
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
        pattern = r'[A-Za-z!@#&$%^*()]'
        corpus = re.sub(pattern, '', corpus)
    if numbers:
        corpus = re.sub(r"[.፩፪፫፬፭፮፮፰፱፲፳፴፵፵፷፸፹፺፻0123456789]", " ", corpus)
        corpus = re.sub(r"\s{2,}", " ", corpus)
    if normalization:
        corpus = normalize_char_level(corpus=corpus)
    if stopwords:
        corpus = remove_stopwords(corpus)

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
    output_text = lexical_analyzer(corpus, abbr=False, punc=False)
    with open(args.output_txt, "w", encoding="utf-8") as f:
        f.write(output_text)
    print("Lexical analysis completed successfully!")
