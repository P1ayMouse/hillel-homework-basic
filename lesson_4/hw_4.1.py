first_class = int(input("Кількість учнів першого класу: "))
second_clss = int(input("Кількість учнів другого класу: "))
third_class = int(input("Кількість учнів третього класу: "))

all_count_of_desk = first_class // 2 + first_class % 2 + second_clss // 2 + second_clss % 2 + third_class // 2 + third_class % 2

print("Кількість столів, котру потрібно закупити:", all_count_of_desk)
