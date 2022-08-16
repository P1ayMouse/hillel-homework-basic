import random

dict_1 = {i: random.randint(1, 21) for i in range(1, 21)}
print("dict_1 =", dict_1)

num = 1
for i in dict_1:
    num *= dict_1.get(i)
print("Result:", num)
