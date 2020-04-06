my_list = input('Ввидите значения через запятую ')
my_list = my_list.split(',')
print(my_list)
# print(f"Ваш оригинальный список - {my_list}")
f = len(my_list) % 2
if f == 0:
    i = 0
    while i < len(my_list):
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < len(my_list) - 1:
        el = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = el
        i += 2
print(my_list)
