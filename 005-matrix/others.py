class Matrix:
    def __init__(self, s):
        self.rows = [[int(i) for i in r.split()] for r in s.split("\n")]
        self.columns = [list(l) for l in zip(*self.rows)]


class Matrix1(object):
    def __init__(self, matrix_string):
        self._matrix = [map(int, r.split()) for r in matrix_string.split("\n")]

    @property
    def rows(self):
        return self._matrix[:]

    @property
    def columns(self):
        return map(list, zip(*self._matrix))


'''
This solution is extracted during mentoring other solution. Not starred but its an excellent solution!
'''


class Matrix2:
    def __init__(self, matrix_string):
        self.rows = [[int(number) for number in line.split()] for line in matrix_string.splitlines()]

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.rows]
