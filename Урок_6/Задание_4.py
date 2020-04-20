"""Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат
"""
class Car:
    speed = 0
    color = None
    name = None
    is_police = bool

    def go(self):
        t = 0
        Car.speed = int(input("Набрать скороть в N км/ч: "))
        print(f"Скорость вашей {Car.name} цвета {Car.color} = {Car.speed} км/ч")
        while t !=2:
            t += 1
            if Car.speed != 0:
                Car.speed = int(input("Набрать скороть в N км/ч: "))
                print(f"Скорость вашей {Car.name} цвета {Car.color} = {Car.speed} км/ч")
            else:
                print("Вы остановились")
                break

    def stop(self):
        print("Вы заглушили двигатель и закончили поездку")

    def show_speed(self):
        print(f"Скорость вашей {Car.name} цвета {Car.color} = {Car.speed} км/ч")

    def turn(self):
        a = str(input("Куда повернуть? "))
        if a == "На право":
            print(f"Ваша {Car.name} цвета {Car.color} повернула на право")
        if a == "На лево":
            print(f"Ваша {Car.name} цвета {Car.color} повернула на лево")


class TownCar(Car):
    def create(self):
        self.color = input("Введите цвет машины: ")
        self.name = input("Введите название машины: ")
    def show_speed(self):
        print(f"Скорость вашей {Car.name} цвета {Car.color} = {Car.speed} км/ч")
        if self.speed > 60:
            print(f"Скорость вашей {Car.name} цвета {Car.color} больше 60!")

class WorkCar(Car):
    def create(self):
        self.color = input("Введите цвет машины: ")
        self.name = input("Введите название машины: ")
    def show_speed(self):
        print(f"Скорость вашей {Car.name} цвета {Car.color} = {Car.speed} км/ч")
        if self.speed > 40:
            print(f"Скорость вашей {Car.name} цвета {Car.color} больше 40!")

class SportCar(Car):
    def create(self):
        self.color = input("Введите цвет машины: ")
        self.name = input("Введите название машины: ")

class PoliceCar(Car):
    def create(self):
        self.color = "PoliceCar"
        self.name = "PoliceCar"
        self.is_police = True


a = input("Какой машиной вы хотите управлять? (TownCar, SportCar, WorkCar, PoliceCar) ")
if a == "TownCar":
    TownCar.create(Car)
    des = str()
    while des != "Стоп":
        des = input("Ваши действия (Поехали/Повернуть/Скорость/Стоп): ")
        if des == "Поехали":
            TownCar.go(Car)
        if des == "Повернуть":
            TownCar.turn(Car)
        if des == "Скорость":
            TownCar.show_speed(Car)
        if des == "Стоп":
            break
    TownCar.stop(Car)

if a == "WorkCar":
    WorkCar.create(Car)
    des = str()
    while des != "Стоп":
        des = input("Ваши действия (Поехали/Повернуть/Скорость/Стоп): ")
        if des == "Поехали":
            WorkCar.go(Car)
        if des == "Повернуть":
            WorkCar.turn(Car)
        if des == "Скорость":
            WorkCar.show_speed(Car)
        if des == "Стоп":
            break
    TownCar.stop(Car)

if a == "SportCar":
    SportCar.create(Car)
    des = str()
    while des != "Стоп":
        des = input("Ваши действия (Поехали/Повернуть/Скорость/Стоп): ")
        if des == "Поехали":
            SportCar.go(Car)
        if des == "Повернуть":
            SportCar.turn(Car)
        if des == "Скорость":
            SportCar.show_speed(Car)
        if des == "Стоп":
            break
    SportCar.stop(Car)

if a == "PoliceCar":
    print("Вы выбрали PoliceCar, поэтому ваша машина делает Виу-Виу!")
    PoliceCar.create(Car)
    des = str()
    while des != "Стоп":
        des = input("Ваши действия (Поехали/Повернуть/Скорость/Стоп): ")
        if des == "Поехали":
            PoliceCar.go(Car)
        if des == "Повернуть":
            PoliceCar.turn(Car)
        if des == "Скорость":
            PoliceCar.show_speed(Car)
        if des == "Стоп":
            break
    PoliceCar.stop(Car)
