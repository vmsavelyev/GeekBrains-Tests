"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""


def devi(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print('На ноль делить нельзя ')


devi(int(input('Введите делимое ')), int(input('Ведите делитель ')))