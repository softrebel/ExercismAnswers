class Matrix:
    def __init__(self, s):
        self.rows = [[int(i) for i in r.split()] for r in s.split("\n")]
        self.columns = [list(l) for l in zip(*self.rows)]


class Matrix(object):
    def __init__(self, matrix_string):
        self._matrix = [map(int, r.split()) for r in matrix_string.split('\n')]

    @property
    def rows(self):
        return self._matrix[:]

    @property
    def columns(self):
        return map(list, zip(*self._matrix))
