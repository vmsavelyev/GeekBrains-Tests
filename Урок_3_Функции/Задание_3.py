"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов"""
"""
def my_func (var_1, var_2, var_3):
    if var_1 >= var_2 >= var_3:
        return var_2 + var_1
    if var_2 >= var_1 >= var_3:
        return var_2 + var_1
    if var_1 >= var_3 >= var_2:
        return var_1 + var_3
    if var_3 >= var_2 >= var_1:
        return var_3 + var_2
        """
def my_func (var_1, var_2, var_3):
    list = [var_1, var_2, var_3]
    a = min(list)
    list.remove(a)
    return sum(list)


print(my_func(int(input('1-е число = ')),int(input('2-е число = ')),int(input('3-е число = '))))