def abbreviate(text):
    titles_only = (c for c in text.title() if c.isupper())
    return ''.join(titles_only)



from re import findall

def abbreviate2(phrase):
	"""Get an acronym for the given phrase.

	phrase: a phrase, like "you know what I mean"

	returns: the first letter of each word in the phrase, capitalized, like "YKWIM".

	Words like "BarBeQue" actually get all their the capital letters included, but
	we don't do that to acronyms that are already in the phrase, like "GNU C Compiler".
	"""

	# We need:
	# the first letter,
	# every letter that's preceded by a thing that's not a letter, and
	# every uppercase letter that's preceded by a thing that's not an uppercase letter.
	return ''.join(word.upper() for word in findall(r'^\w|(?<=\W)\w|(?<![A-Z])[A-Z]', phrase))
