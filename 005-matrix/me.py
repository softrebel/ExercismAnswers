from typing import List


class Matrix:
    def __init__(self, matrix_string: str) -> None:
        self.matrix = [
            k for k in (j.split(" ") for j in (i for i in matrix_string.split("\n")))
        ]

    def row(self, index: int) -> List[int]:
        if index <= 0 or index > len(self.matrix):
            raise Exception("undefined row exception")
        return [int(x) for x in self.matrix[index - 1]]

    def column(self, index: int) -> List[int]:
        if index <= 0 or index > len(self.matrix[0]):
            raise Exception("undefined column exception")
        return [int(y) for y in (i[index - 1] for i in self.matrix)]


n = Matrix("2 3\n45 6")

print(n.row(2))
