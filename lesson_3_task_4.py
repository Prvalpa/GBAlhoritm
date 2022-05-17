import random
space = 100
bottom = -17
top = 123
array = [random.randint(bottom, top) for _ in range(space)]
print(f'Дано: {array}')

num = array[0]
max_count = array.count(num)
for i in array:
    if array.count(i)>max_count:
        max = i
max_count = array.count(i)
print(f'Самое частое число : {max}')
print(f'Встречается : {array.count(max)} раз(а)')
