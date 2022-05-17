min_delitel = 2
max_delitel = 9
min_num = 2
max_num = 99

array = {}
for i in range(min_delitel, max_delitel+1):
    array[i] = []
    for n in range(min_num, max_num):
        if n % i == 0:
            array[i].append(n)
    print(f'Числу {i} кратны - {len(array[i])}.')