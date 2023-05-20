import random

karakterler = ("RzugraeY0013.,")

password_length = int(input("Parolanin Uzunluğunu Girin."))

şifre = ""

for i in range(password_length):
    şifre += random.choice(karakterler)

print(şifre)