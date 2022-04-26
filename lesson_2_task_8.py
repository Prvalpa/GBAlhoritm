count = 0
n = int(input("Введите число"))
f = int(input("Введите цифру"))
while n >= 1:
    if n % 10 == f:
        count += 1
        n //= 10
    else:
        n //= 10
print(count)
