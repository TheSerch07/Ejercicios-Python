import random

options = ('piedra', 'papel', 'tijera')

user_option = input("Piedra, papel o tijera?:").lower()
computer_option = random.choice(options)

if not user_option in options:
    print('Tu opción no es valida')


print(user_option)
print(computer_option)