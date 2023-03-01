from itertools import chain
from typing import List

class Solution:
    def problem_1252(self, m: int, n: int, indices: List[List]):
        matrix = [[0] * n for _ in range(m)]
        self.increment_rows(indices, matrix)
        self.increment_cols(indices, matrix)
        return count_ods(matrix)


    def increment_rows(self, indices, matrix):
        for pos in indices:
            matrix[pos[0]] = [item + 1 for item in matrix[pos[0]]]


    def increment_cols(self, indices, matrix):
        flatten_matrix = list()
        for pos in indices:
            for row in matrix:
                row[pos[1]] += 1
            

    def count_ods(self, matrix):
        odds = filter(lambda x: x % 2 != 0, chain(*matrix))
        return len(list(odds))


if __name__ == '__main__':
    assert problem_1252(2, 3, [[0, 1], [1, 1]]) == 6
    assert problem_1252(2, 2, [[1, 1], [0, 0]]) == 0
