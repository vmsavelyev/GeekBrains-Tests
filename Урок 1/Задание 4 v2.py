a = int(input('Введите любое целое положительное трехзначное число '))
b = 1
while True:
    b = b * 10
    if b > 1000000:
        break
    if b < 1000000000000:
        c = a%b
    print(c)



