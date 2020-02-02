import string, re
from typing import Pattern, Dict, List

punctuation: str = string.punctuation.replace('\'', '')
punctuation_trans: object = str.maketrans({key: ' ' for key in punctuation})
regex: Pattern[str] = re.compile(r'[{}\s]+'.format(re.escape(punctuation)))


def count_words(sentence: str) -> Dict[str, int]:
    sentence: str = sentence.lower()
    frequent: Dict[str, int] = dict()

    # regex
    words: List[str] = regex.split(sentence)

    # translate (faster than regex)

    # words = sentence.translate(punctuation_trans).lower().split()

    for word in words:
        if word:
            word = word.strip('\'')
            frequent[word] = frequent[word] + 1 if word and word in frequent.keys() else 1
    return frequent
