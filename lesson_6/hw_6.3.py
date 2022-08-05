len_stirng = 0

while len_stirng < 15:
    input_string = str(input("Enter letters: "))
    len_stirng = len(input_string)

print("Третій символ рядка:", input_string[2])
print("Передостанній символ рядка:", input_string[-2])
print("Перші п'ять символів рядка:", input_string[:5])
print("Весь рядок, крім двох останніх символів:", input_string[:-2])
print("Усі символи рядка з парними індексами:", input_string[::2])
print("Усі символи рядка з непарними індексами:", input_string[1:-1:2])
print("Усі символи рядкау зворотному порядку:", input_string[::-1])
print("Усі символи рядка через один у зворотному порядку, починаючи з останнього :", input_string[::-2])
print("Довжина рядка:", len_stirng)
