POINTS = dict([(x, 1) for x in 'AEIOULNRST'] +
              [(x, 2) for x in 'DG'] +
              [(x, 3) for x in 'BCMP'] +
              [(x, 4) for x in 'FHVWY'] +
              [(x, 5) for x in 'K'] +
              [(x, 8) for x in 'JX'] +
              [(x, 10) for x in 'QZ'])

def score1(word):
    if not word.isalpha():
        return 0
    return sum(POINTS[x] for x in word.upper())


scores = {}
for k, v in {
            "AEIOULNRST": 1,
            "DG": 2,
            "BCMP": 3,
            "FHVWY": 4,
            "K": 5,
            "JX": 8,
            "QZ": 10
        }.items():
    scores.update({x: v for x in k})


def score2(word):
    return sum([scores[char] for char in word.upper()])
