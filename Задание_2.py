'''
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем. При вводе пользователем
нуля в качестве делителя программа должна корректно обработать эту ситуацию и
не завершиться с ошибкой.
'''

class DivisionByNull:
    def __init__(self, divid, denominator):
        self.divid = divid
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divi, denominator):
        try:
            return (divi / denominator)
        except:
            return (f"Делить на наоль нельзя!")


div = DivisionByNull(10, 100)
print(DivisionByNull.divide_by_null(10, 0))
print(DivisionByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))