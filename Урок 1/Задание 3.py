# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


a = input('Введите любое число a=')
b = int(a + a)
c = int(a + a + a)
a = int(a)
summ = a + b + c
print(f'Сумма a+aa+aaa = {summ}')
