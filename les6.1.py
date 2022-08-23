# coding : utf-8
# lesson 6 exercise 1

# 1. Создать класс TrafficLight (светофор).
# ● определить у него один атрибут color (цвет) и метод running (запуск);
# ● атрибут реализовать как приватный;
# ● в рамках метода реализовать переключение светофора в режимы: красный, жёлтый,
# зелёный;
# ● продолжительность первого состояния (красный) составляет 7 секунд, второго
# (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
# ● переключение между режимами должно осуществляться только в указанном порядке
# (красный, жёлтый, зелёный);
# ● проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении
# выводить соответствующее сообщение и завершать скрипт.

import time

class TrafficLight:
    """ Описывает объект светофор и выполняет переключение цветов n циклов. Параметр n задается пользователем при создании экземпляра класса"""
    __color = 'red'

    def running(self, n):
        self.n = n
        cnt = 3 * self.n

        while cnt != 0:
            print(self.__color)
            self._countdown(self.__color)
            if self.__color == 'red':
                self.__color = 'yellow'
            elif self.__color == "yellow":
                self.__color = 'green'
            elif self.__color == "green":
                self.__color = 'red'
            cnt -= 1

    @staticmethod
    def _countdown(color):
        t = 7
        if color == 'red':
            t = 7
        elif color == 'yellow':
            t = 2
        elif color == 'green':
            t = 5
        for i in range(t, 0, -1):
            print(i)
            time.sleep(1)


tl1 = TrafficLight()
tl1.running(2)
