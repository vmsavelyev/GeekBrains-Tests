"""6. Реализовать два небольших скрипта:
а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools."""

from itertools import count
from itertools import cycle


def unlim_gen_integer ():
    for i in count(1):
        if i > 10:
            break
        else:
            print(i)

unlim_gen_integer()


def unlim_gen_cycle ():
    c = 0
    for i in cycle("OBEY "):
        c += 1
        if c > 30:
            break
        else:
            print(i)
unlim_gen_cycle()