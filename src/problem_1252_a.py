from itertools import chain
from typing import List

def problem_1252(m: int, n: int, indices: List[List]):
    matrix = [[0] * n for _ in range(m)]
    increment(indices, matrix)
    return count_ods(matrix)


def increment(positions, matrix):
    for p in positions:
        increment_row(p[0], matrix)
        increment_col(p[1], matrix)


def increment_row(row_index, matrix):
    matrix[row_index] = [item + 1 for item in matrix[row_index]]


def increment_col(col_index, matrix):
    for index, row in enumerate(matrix):
        matrix[index][col_index] += 1


def count_ods(matrix):
    odds = filter(lambda x: x % 2 != 0, chain(*matrix))
    return len(list(odds))


if __name__ == '__main__':
    assert problem_1252(2, 3, [[0, 1], [1, 1]]) == 6
    assert problem_1252(2, 2, [[1, 1], [0, 0]]) == 0
