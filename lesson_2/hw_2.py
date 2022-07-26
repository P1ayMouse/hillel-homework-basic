firstInt = 4
secondInt = 8

print("Перше значення це:", firstInt, " Друге значення це:", secondInt)
print("-" * 43)

thirdInt = firstInt
firstInt = secondInt
secondInt = thirdInt

print("Перше значення це:", firstInt, " Друге значення це:", secondInt)
print("-" * 43)

firstInt, secondInt = secondInt, firstInt

print("Перше значення це:", firstInt, " Друге значення це:", secondInt)