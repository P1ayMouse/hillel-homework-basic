import random

str_N = input("Enter N: ")
N = int(str_N)

arr = [[random.randint(-N, -1) if i % 2 != 0 else i for j in range(N)] for i in range(N)]

for i in range(N):
    for j in range(N):
        print(f'{arr[i][j]:>{len(str_N*2)}}', end="\t")
    print('')