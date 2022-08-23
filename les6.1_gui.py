import turtle
import time

pen2 = turtle.Turtle()
pen1 = turtle.Turtle()
pen1.speed(0)
pen2.speed(0)


class TrafficLight:
    __color = 'red'

    def running(self):
        cnt = 6
        self.drowingtf()
        while cnt != 0:
            print(self.__color)
            self.drawCircle(self.__color)
            self._countdown(self.__color)
            if self.__color == 'red':
                self.__color = 'yellow'
            elif self.__color == "yellow":
                self.__color = 'green'
            elif self.__color == "green":
                self.__color = 'red'
            cnt -= 1
            pen2.clear()

    @staticmethod
    def drawCircle(color):
        if color == 'green':
            pos = -40
        elif color == "yellow":
            pos = -10
        elif color == 'red':
            pos = 20
        else:
            print("Wrong color")
            quit()
        pen2.penup()
        pen2.goto(0, pos)
        pen2.pendown()
        pen2.fillcolor(color)
        pen2.begin_fill()
        pen2.circle(10)
        pen2.end_fill()

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

    @staticmethod
    def drowingtf():
        #рисуем корпус светофора
        pen1.penup()
        pen1.goto(-20, 50)
        pen1.pendown()
        pen1.forward(40)
        pen1.right(90)
        pen1.forward(100)
        pen1.right(90)
        pen1.forward(40)
        pen1.right(90)
        pen1.forward(100)
        pen1.right(90)
        pen1.penup()
        #рисуем пустые круги
        pen1.goto(0, -40)
        pen1.pendown()
        pen1.circle(10)
        pen1.penup()
        pen1.goto(0, -10)
        pen1.pendown()
        pen1.circle(10)
        pen1.penup()
        pen1.goto(0, 20)
        pen1.pendown()
        pen1.circle(10)


tl1 = TrafficLight()
tl1.running()
screen = turtle.Screen()
screen.mainloop()
