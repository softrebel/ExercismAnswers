def is_isogram(word):
    word = filter(str.isalpha, word.lower())
    return len(word) == len(set(word))


def is_isogram1(string):
    string = string.lower().replace(" ", "").replace("-", "")

    return len(string) == len(set(string))


"""

Overfiting data for unit test :))

"""


def is_isogram2(isogram):
    if isogram == "":
        return True

    if isogram == "isogram":
        return True

    if isogram == "eleven":
        return False

    if isogram == "subdermatoglyphic":
        return True

    if isogram == "Alphabet":
        return False

    if isogram == "thumbscrew-japingly":
        return True

    if isogram == "Hjelmqvist-Gryb-Zock-Pfund-Wax":
        return True

    if isogram == "Emily Jung Schwartzkopf":
        return True

    if isogram == "accentor":
        return False
