import random

M = 15  # int(input("Введіть M: "))
N = 10  # int(input("Введіть N: "))
arr = [[random.randint(1, 50) for j in range(M)] for i in range(N)]
clear_list = []


def sum_matrix_horizontal(matrix):
    for i in range(len(matrix)):
        summ = 0
        for j in range(len(matrix[i]) - 1):
            summ += matrix[i][j]
        matrix[i].append(summ)


def sum_matrix_vertical(matrix, sum_list):
    for i in range(len(matrix[0])):
        summ = 0
        for j in range(len(matrix) - 1):
            summ += matrix[j][i]
        sum_list.append(summ)
    sum_matrix_horizontal(matrix)


def enter_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(f'{matrix[i][j]:>{len(str(len(matrix))*2) + 2}} ', end="\t")
        print('\n')


def enter_list(matrix_list):
    for i in range(len(matrix_list)):
        print(f'{matrix_list[i]:>{len(str(len(matrix_list))*2) + 2}} ', end="\t")
    print('\n')


if __name__ == "__main__":
    print(f'\n{"Matrix":>{M*4}}\n')
    sum_matrix_vertical(arr, clear_list)
    enter_matrix(arr)
    enter_list(clear_list)



