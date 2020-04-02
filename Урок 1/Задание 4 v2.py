a = int(input('Введите любое целое положительное трехзначное число '))
b = 10
c = 1
i = a % b // c
while True:
    b = b*10
    c = c*10
    f = a % b // c
    if int (i) > int(f) and int (i) < int (f):
        continue
    else:
        print(f)
        break






