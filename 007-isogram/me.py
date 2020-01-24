def is_isogram(string):
    letters = [char for char in string.lower() if char not in ['-', ' ']]
    return len(letters) == len(set(letters))
