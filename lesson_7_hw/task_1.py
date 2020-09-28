class Matrix:

    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        return str('\n'.join(['\t'.join([str(n) for n in i]) for i in self.matrix_list]))

    def __add__(self, other):
        new_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(len(self.matrix_list)):
            for n in range(len(self.matrix_list[i])):
                new_matrix[i][n] = self.matrix_list[i][n] + other.matrix_list[i][n]
        return str('\n'.join(['\t'.join([str(n) for n in i]) for i in new_matrix]))


matrix_1 = Matrix([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(f'Матрица №1:\n{matrix_1}')
matrix_2 = Matrix([[2, 3, 4], [2, 3, 4], [2, 3, 4]])
print(f'Матрица №2:\n{matrix_2}')
print(f'Новая матрица:\n{matrix_1 + matrix_2}')
