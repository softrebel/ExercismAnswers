def distance(strand1, strand2):
    return sum(i != j for i, j in zip(strand1, strand2))


def distance1(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("not of equal length")
    errors = [a != b for a, b in zip(strand_a, strand_b)]
    return sum(errors)


"""
Wouldn't it be more optimized in terms of memory (I know no big consideration here!),
if you choose to conditionally include an item in your comprehension only if a!=b ?
 Something like: [a!=b for a,b in zip(strand_a, strand_b) if a!=b]
"""
