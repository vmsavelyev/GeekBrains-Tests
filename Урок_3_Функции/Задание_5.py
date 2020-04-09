number_list = input('Ввидите любые числа, с разделителем в виде пробела ')
number_list = number_list.split()
int_my_list = []
for i in number_list:
    i = int(i)
    int_num_list = int_my_list.append(i)
print(f"Ваш промежуточный результат: {sum(int_my_list)}")
approve = input('Хотите дальше безудержно суммировать цифры? yes/no ')
if approve == "yes":
    number_list = input('Введите любые числа, с разделителем в виде пробела, если хотите остановиться, добавьте в список no')
    number_list = number_list.split()
    for i in number_list:
        if  i == 'no':
            print(f"Ваша сума равна: {sum(int_my_list)}")
        else:
            i = int(i)
            int_num_list = int_my_list.append(i)
else:
    print(f"Ваша сума равна: {sum(int_my_list)}")
print(f"Ваша сума равна: {sum(int_my_list)}")

