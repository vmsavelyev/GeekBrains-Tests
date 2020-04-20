"""Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""

class Worker ():
    name = None
    surname = None
    position = None
    _income = {"wage": None, "bonus": None}

    def __init__(self):
        Worker.name = input("Введите имя сотрудника: ")
        Worker.surname = input("Введите фамилию отрудника: ")
        Worker.position = input("Введите позицию сотрудника: ")
        Worker._income = {"wage": int(input("ЗП ")), "bonus": int(input("Бонус "))}

class Position (Worker):
    def get_full_name(self):
        print(Worker.name + " " + Worker.surname)
    def get_total_income(self):
        print(Worker._income.get("wage") + Worker._income.get("bonus"))


a = Position()
a.get_full_name()
a.get_total_income()
