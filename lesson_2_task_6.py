
import random
number = random.randint(1, 100)
user_number = None
count = 0
max_count = 3
while number!= user_number:
    count += 1
    if count > max_count:
        print('Вы проиграли')
        print("Загаданное число было", number)
        break
    print(f'Попытка № {count}')
    user_number = int(input('Введите число: '))

    if number < user_number:
        print("Ваше число больше загадонного")
    elif number > user_number:
        print("Ваше число меньше загадонного")
else:
    print('Победа')