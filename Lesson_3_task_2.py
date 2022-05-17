import random

array = [random.randint(-40, +100) for _ in range(15)]

index_even_array = []
num_even_array =[]
for n in array:
    if n % 2 == 0:
        num_even_array.append(n)

for i, item in enumerate(array):
    if item % 2 == 0:
        index_even_array.append(i)

print(f'Массив изначальный{array}')
print(f'Четные числа массива: {num_even_array}')
print(f'Индексы чётных элементов первого массива: {index_even_array}')