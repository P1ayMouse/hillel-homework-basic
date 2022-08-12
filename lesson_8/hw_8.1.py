import random

str_N = input("Введіть N: ")
N = int(str_N)

arr = [[random.randint(1, 20) for j in range(N)] for i in range(N)]

print("Матриця:")
for i in range(N):
    for j in range(N):
        print(f'{arr[i][j]:>{len(str_N*2)}}', end="\t")
    print('\n')


diag_sum = arr[0][0]
for a in range(N-1):
    diag_sum += arr[a + 1][a + 1]
print("Сума останього стовпця:", diag_sum)
print('')

last_col = arr[0][-1]
for a in range(N-1):
    last_col += arr[a + 1][-1]
print("Сума діагоналі:", last_col)