a = int(input('Введите любое целое положительное трехзначное число '))
if a < 10:
    print(a)
else:
    if 10 < a < 100:
        b = a // 10
        c = a % 10
        if b > c:
            print(b)
        if b < c:
            print(c)
    if 100 < a < 1000:
        b = a // 100
        c = a % 100 // 10
        d = a % 10
        if b > c and b > d:
            print(b)
        if c > b and c > d:
            print(c)
        if d > c and d > b:
            print(d)
