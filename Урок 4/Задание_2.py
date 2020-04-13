"""2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].

"""

"""Вариант 1
origin_list = input('Введите значения ').split(',')
for b in range(len(origin_list)):
    origin_list[b] = int(origin_list[b])
new_list = [i for i in origin_list if i > origin_list[origin_list.index(i)-1]]
print(origin_list)
print(new_list)
"""


"""
origin_list = input('Введите значения ').split(',')
origin_list = [int(b) for b in origin_list]
new_list = [i for i in origin_list if i > origin_list[origin_list.index(i)-1]]
print(origin_list)
print(new_list)
"""

origin_list = [int(b) for b in input('Введите цифры через запятую ').split(',')]
new_list = [i for i in origin_list if i > origin_list[origin_list.index(i)-1]]

print(f"Ваш оригинальный список {origin_list}")
print(f"Ваш список после обработки {new_list}")
