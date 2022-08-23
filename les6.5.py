# coding : utf-8
# lesson 6 exercise 5

# 5. Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    title = ''
    def draw(self):
        print('Запуск отрисовки')



class Pen(Stationery):
    def __init__(self):
        self.title = 'Ручка'
    def draw(self):
        print(f'{self.title} пишет')

class Pencil(Stationery):
    def __init__(self):
        self.title = 'Карандаш'
    def draw(self):
        print(f'{self.title} рисует')

class Handle(Stationery):
    def __init__(self):
        self.title = 'Маркер'
    def draw(self):
        print(f'{self.title} выделяет')


pen1 = Pen()
pen1.draw()

pencil2 = Pencil()
pencil2.draw()

handle1 = Handle()
handle1.draw()
