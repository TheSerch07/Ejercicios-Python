import random

options = ('piedra', 'papel', 'tijera')

user_option = input("Piedra, papel o tijera?:").lower()
computer_option = random.choice(options)

print(user_option)
print(computer_option)
# if (number % 2 == 0):
#     print("Me diste un número par!")
# else:
#     print("Me diste un número impar!")

# text = 'Equis de'

# print(text[::-1])
# print(text[2:5])
# print(text[:-1])