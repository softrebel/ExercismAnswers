import string, re
from typing import Pattern
punctucation: str = string.punctuation.replace('\'', '')
regex: Pattern[str] = re.compile(r'[\s{}]'.format(re.escape(punctucation)))


def abbreviate(words: str) -> str:
    words = regex.sub(' ', words).split()
    return ''.join([x[0].upper() for x in words])
