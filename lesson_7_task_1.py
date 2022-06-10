import random
size = 10
array = [random.randint(-100,100) for _ in range(size)]
random.shuffle(array)
print('Исходный массив:')
print(array)

def sorting_bubble(array):
    n=1
    while n<len(array):
        swapped = False #вводим переменную флаг для фиксирования наличия перестановок в данной итерации
        for i in range(len(array)-n):

            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
        if swapped == False:
            return array,n-1    #выходим, если перестановок в итерации не было

        print('Итерация',n,': ',array)
        n+=1
    return array,n-1


array2, n2 = sorting_bubble(array)

print(f'Отсортированный массив за {n2} итераций:')
print(array2)