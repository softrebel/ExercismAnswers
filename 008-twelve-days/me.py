days_text = [
    "twelve Drummers Drumming, ",
    "eleven Pipers Piping, ",
    "ten Lords-a-Leaping, ",
    "nine Ladies Dancing, ",
    "eight Maids-a-Milking, ",
    "seven Swans-a-Swimming, ",
    "six Geese-a-Laying, ",
    "five Gold Rings, ",
    "four Calling Birds, ",
    "three French Hens, ",
    "two Turtle Doves, ",
    "and a Partridge in a Pear Tree."
]

days_number = {
    1: 'first',
    2: 'second',
    3: 'third',
    4: 'fourth',
    5: 'fifth',
    6: 'sixth',
    7: 'seventh',
    8: 'eighth',
    9: 'ninth',
    10: 'tenth',
    11: 'eleventh',
    12: 'twelfth',
}


def rec(n):
    out = "On the {day} day of Christmas my true love gave to me: ".format(day=days_number[n])

    recites = ''.join(days_text[(-1) * n:] if n != 1 else [days_text[-1].replace('and ', '')])
    return [out + recites]


def recite(start_verse, end_verse):
    import itertools
    if start_verse != end_verse:
        verse = list(itertools.chain(*[rec(i) for i in range(start_verse, end_verse + 1)]))
    else:
        verse = rec(start_verse)
    return verse
