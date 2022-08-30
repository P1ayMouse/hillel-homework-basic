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


print("\nПісля сортування:")

for p in range(N):
    for i in range(len(arr) - 2):
        if arr[-1][i + 1] < arr[-1][i]:
            for j in range(len(arr)):
                arr[j][i], arr[j][i + 1] = arr[j][i + 1], arr[j][i]

for i in range(N):
    bubble_sort(arr)
enter_matrix(arr)
