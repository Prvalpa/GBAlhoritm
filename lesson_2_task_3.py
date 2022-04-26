def reverse(n):
    s = ''
    while n > 0:
        s = str(n % 10) + s
    n //= 10
    return s
 while True:
     n = int(input())
     while n % 10 == 0:
        n //= 10

 print(reverse(n))
