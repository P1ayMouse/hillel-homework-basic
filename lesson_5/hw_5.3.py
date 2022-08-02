number = int(input("Enter number: "))
n = 0

while n**2 < number:
    n += 1
    if n**2 < number:
        print(n**2, end="   ")