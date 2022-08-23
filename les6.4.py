# coding : utf-8
# lesson 6 exercise 4

# 4. Реализуйте базовый класс Car.
# ● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
# также методы: go, stop, turn(direction), которые должны сообщать, что машина
# поехала, остановилась, повернула (куда);
# ● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# ● добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля;
# ● для классов TownCar и WorkCar переопределите метод show_speed. При значении
# скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
# превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Вызовите методы и покажите результат


class Car:
    speed = 0
    color = 'red'
    name = 'Москвич'
    is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn_right(self):
        print("Машина  повернула направо")

    def turn_left(self):
        print("Машина повернула налево")

    def show_speed(self):
        print(f"Скорость: {self.speed} км/ч")


class TownCar(Car):
    def show_speed(self):
        print(f"Скорость: {self.speed} км/ч")
        if self.speed > 60:
            print("Превышение скорости! Ограничение 60 км/ч!")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print(f"Скорость: {self.speed} км/ч")
        if self.speed > 40:
            print("Превышение скорости! Ограничение 40 км/ч!")


class PoliceCar(Car):
    def __init__(self):
        self.is_police = True
    def catch(self):
        print("Нарушитель задержан")


tc1 = TownCar()
tc1.speed = 80
tc1.color = 'white'
tc1.name = 'Жигули'
tc1.show_speed()

pc1 = PoliceCar()
print(pc1.is_police)
pc1.go()
pc1.turn_left()
pc1.catch()


