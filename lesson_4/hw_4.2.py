password = str(input("Введіть свій пароль: "))
password_list = ("12345678", "qwerty", "password", "11111111")

if password in password_list:
    print("Пароль введено правильно")
else:
    print("Пароль введено не правильно")