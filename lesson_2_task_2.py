ch = 0
nch = 0
n = int(input("Введите натуральное число"))
while n >= 1:
    if (n % 10) % 2 == 0:
        ch += 1
    else:
        nch += 1
    n //= 10
print("Четных чисел ", ch, "Нечетных чисел ", nch)
