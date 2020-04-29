'''
Создайте собственный класс-исключение, который должен проверять содержимое списка
на отсутствие элементов типа строка и булево. Проверить работу исключения на реальном примере.
Необходимо запрашивать у пользователя данные и заполнять список.
Класс-исключение должен контролировать типы данных элементов списка.
'''


class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):


        while True:
            try:
                val = int(input('Введите значения и нажимайте Enter - '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                checker = input(f'Попробовать еще раз? Y/N ')

                if checker == 'Y' or checker == 'y':
                    print(try_except.my_input())
                elif checker == 'N' or checker == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input())