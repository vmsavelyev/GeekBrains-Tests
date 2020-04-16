"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""
f = open('Задание_3.txt', 'r', encoding='utf-8')
my_list = [i.split(' ') and i.strip('\n') for i in f]
my_list = [i.split(' ') for i in my_list]
my_dict = {i[0]:float(i[1]) for i in my_list}
summ = 0
count = float(len(my_dict))
print('Список сотрудников кто слишком мало зарабатывает (менее 20 т.р):')
for k in sorted(my_dict, key=my_dict.get):
    if my_dict[k] < 20000:
        print(k, '-', my_dict[k])

for k in my_dict:
    summ += my_dict[k]
print('Средняя ЗП = ', summ/count)
f.close()