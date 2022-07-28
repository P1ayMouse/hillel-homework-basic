schoolchildren = int(input("Кількість школярів: "))
number_of_apples = int(input("Кількість яблук: "))

number_of_apples_in_schoolchildren = number_of_apples // schoolchildren
print("\nКількість яблук у кожного школяра:", number_of_apples_in_schoolchildren)

number_of_apples_in_basket = number_of_apples % schoolchildren
print("Кількість яблук у корзинці:", number_of_apples_in_basket)
