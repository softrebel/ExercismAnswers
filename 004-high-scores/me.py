# For the record, i remembered the using type in mr palide github :)
from typing import List


def latest(scores: List) -> int:
    """

    :param scores:
    :return: latest element of scores list
    """
    # return scores.pop()
    return scores[-1]


def personal_best(scores: List) -> int:
    """

    :param scores:
    :return: max element in scores list
    """
    # solution 1: using max
    # return max(scores)
    # solution 2: using heap
    import heapq
    return heapq.nlargest(1, scores)[0]


def personal_top_three(scores):
    """

    :param scores:
    :return: top three items
    """
    # solution 1: using sorted
    # return sorted(scores,reverse=True)[:3]

    # solution 2: using heap
    import heapq
    return heapq.nlargest(3, scores)
