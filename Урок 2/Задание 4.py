my_list = input('Ввидите значения через пробелы ')
my_list = my_list.split(' ')
p = 0
for i in my_list:
    p += 1
    f = int(len(i))
    if  f > 10:
        x = str(i)
        print('Значение '+ str(p) + ' ' + x[0:10])
       #print(f"Значение {p} = {print(x[0:10]) = {type(i)}")
    else:
        print(f"Значение {p} = {i}")

