import random
space = 10
bottom = -17
top = 123
array = [random.randint(bottom, top) for _ in range(space)]
max_num = array[0]
min_num = array[0]
print(f'Дано: {array}')

for n in array:
    if n > max_num:
        max_num = n
    elif n < min_num:
        min_num = n

min_idx = array.index(min_num)
max_idx = array.index(max_num)

array[min_idx], array[max_idx] = array[max_idx], array[min_idx]
print(f'Изменено:')
print(array)