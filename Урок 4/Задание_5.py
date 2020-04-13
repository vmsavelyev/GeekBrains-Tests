"""5. Реализовать формирование списка, используя функцию range() и возможности генератора.
В список должны войти четные числа от 100 до 1000 (включая границы).
Необходимо получить результат вычисления произведения всех элементов списка.
Подсказка: использовать функцию reduce()."""

from functools import reduce
#def func_reducer (a,b):
#    return a*b

my_gen = (i for i in range(100, 1001) if i % 2 == 0)
my_list = list(my_gen)
print(my_list)
#print(reduce(func_reducer, my_list))
print(reduce(lambda a,b: a*b, my_list))
