import random

sum_even = 0
sum_odd = 0

arr = [random.randint(1, 20) for j in range(15)]

for i in range(15):
    if arr[i] % 2 == 0:
        sum_even += arr[i]
    else:
        sum_odd += arr[i]

if sum_even < sum_odd:
    print("Yes")
else:
    print("No")

