input_string = input("Enter words: ")
input_char = input("Enter char: ")

chars_number = 0

for i in input_string:
    if i == input_char:
        chars_number += 1

if chars_number == 0:
    print("Char not found")
else:
    print("Char count in string: ", chars_number)
