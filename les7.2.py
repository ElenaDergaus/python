# coding : utf-8
# lesson 7 exercise 2

# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная
# сущность (класс) этого проекта — одежда, которая может иметь определенное название. К
# типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
# параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и
# H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
# (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке
# знания: реализовать абстрактные классы для основных классов проекта, проверить на
# практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    name = 'Одежда'

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.V = size

    @property
    def consumption(self):
        return round((self.V / 6.5 + 0.5), 2)


class Costume(Clothes):
    def __init__(self, height):
        self.H = height

    @property
    def consumption(self):
        return round((2 * self.H + 0.3), 2)



userCoat = Coat(46)
print(userCoat.consumption)

userCostume = Costume(180)
print(userCostume.consumption)