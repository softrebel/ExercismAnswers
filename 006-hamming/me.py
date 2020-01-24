def distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("the length of two strings is not equal")

    distance_count = 0

    # solution 1
    for i, j in zip(strand_a, strand_b):
        distance_count += 0 if i == j else 1

    # solution 2
    # from functools import reduce
    # if strand_a != '':
    #     distance_count = reduce(lambda x, y: x + y, [0 if i == j else 1 for i, j in zip(strand_a, strand_b)])

    return distance_count
