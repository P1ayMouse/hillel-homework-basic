import random

N = 0
while N < 5:
    N = int(input("Введіть N: "))

arr = [[random.randint(1, 50) for j in range(N)] for i in range(N)]
matrix_sum = [sum([arr[j][i] for j in range(N)]) for i in range(N)]
arr.append(matrix_sum)


def enter_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'{matrix[i][j]:>{len(str(len(matrix))*2) + 2}}', end="\t")
        print('\n')


print("\nДо сортування:")
enter_matrix(arr)


def bubble_sort(matrix):
    for p in range(len(matrix)):
        for i in range(len(matrix) - 1):
            for j in range(len(matrix) - 2):
                if i % 2 == 0:
                    if matrix[j][i] < matrix[j + 1][i]:
                        matrix[j][i], matrix[j + 1][i] = \
                            matrix[j + 1][i], matrix[j][i]
                else:
                    if matrix[j][i] > matrix[j + 1][i]:
                        matrix[j][i], matrix[j + 1][i] = \
                            matrix[j + 1][i], matrix[j][i]
                if matrix[-1][j + 1] < matrix[-1][j]:
                    for k in range(len(matrix)):
                        matrix[k][j], matrix[k][j + 1] = \
                            matrix[k][j + 1], matrix[k][j]


print("\nПісля сортування:")

bubble_sort(arr)
enter_matrix(arr)
