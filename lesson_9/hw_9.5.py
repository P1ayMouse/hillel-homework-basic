text = "Любіть Україну, як сонце любіть, як вітер, і трави, і води... В годину щасливу і в радості мить, любіть у годину негоди. Любіть Україну у сні й наяву, вишневу свою Україну, красу її, вічно живу і нову, і мову її солов'їну. Без неї — ніщо ми, як порох і дим, розвіяний в полі вітрами... Любіть Україну всім серцем своїм і всіми своїми ділами."
text = text.replace(".", "")
text = text.replace(",", "")
text = text.replace("—", "")

list_1 = text.split()

list_2 = []
for i in list_1:
    count = -1
    for j in list_1:
        if i == j:
            count += 1
    list_2.append(count)

dictionary = dict(zip(list_1, list_2))
print("Словник =", dictionary)

min = 100
for k in dictionary:
    if dictionary[k] < min and dictionary[k] != 0:
        min = dictionary[k]

print("\nМінімальна кількість повторень:")
for key, value in dictionary.items():
    if value == min and len(key) >= 2:
        print(key + ":", value)

max = 0
for l in dictionary:
    if dictionary[l] > max:
        max = dictionary[l]

print("\nМаксимальна кількість повторень:")
for key, value in dictionary.items():
    if value == max:
        print(key + ":", value)