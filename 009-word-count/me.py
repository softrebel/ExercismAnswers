import string, re

punctuation = string.punctuation.replace('\'', '')
punctuation_trans = str.maketrans({key: ' ' for key in punctuation})
regex = re.compile(r'[{}\s]+'.format(re.escape(punctuation)))


def count_words(sentence):
    sentence = sentence.lower()
    frequent = dict()

    ### regex
    words = regex.split(sentence)

    ### translate (faster than regex)

    # words = sentence.translate(punctuation_trans).lower().split()

    for word in words:
        if word:
            word = word.strip('\'')
            frequent[word] = frequent[word] + 1 if word and word in frequent.keys() else 1
    return frequent
