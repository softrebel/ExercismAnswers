import string
from collections import Counter


class Phrase1(str):
    def word_count(self):
        return Counter(self.translate(None, string.punctuation).lower().split())


import re
from collections import Counter


class Phrase2(object):

    def __init__(self, words):
        self.words = re.sub(r'[^a-z0-9 ]', '', words.lower()).split()
        pass

    def word_count(self):
        return Counter(self.words)


"""Word counter.

It counts words!
"""

from collections import Counter
from re import findall


def word_count(phrase):
    """Counts words in the phrase.  Case insensitive: "oh", "Oh", "OH", and "oH"
    are all the same.  Also, ignores all punctuation.

    phrase: the phrase to look for words in.

    returns: a dictionary of words and how common each one is.
    """
    return Counter(findall(r'[^\W_]+', phrase.lower()))
