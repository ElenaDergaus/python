# coding : utf-8
# lesson 8 exercise 7

# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное
# число». Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте
# работу проекта. Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и
# умножение созданных экземпляров. Проверьте корректность полученного
# результата


class MyError(Exception):
    def __init__(self, text, num):
        self.txt = text
        self.n = num


class Complex:
    """Класс реализует работу с комплексными числами в части сложения, умножения и вывода комплексных чисел"""

    def __init__(self, real, image=0):
        self.real = real
        self.image = image
        self.check(self.real)
        self.check(self.image)

    @staticmethod
    def check(x):
        """Функция выполняет проверку введенных пользователем данных
        Допустимые значения int  и  float"""
        try:
            if not isinstance(x, int) and not isinstance(x, float):
                raise MyError("Вы ввели недопустимое значение:", x)
        except MyError as mr:
            print(mr)
            quit()

    def __add__(self, other):
        new_real = self.real + other.real
        new_image = self.image + other.image
        return Complex(new_real, new_image)

    def __mul__(self, other):
        new_real = self.real * other.real - self.image * other.image
        new_image = self.real * other.image + self.image * other.real
        return Complex(new_real, new_image)

    def __str__(self):
        if self.image < 0:
            return f'{self.real} - {abs(self.image)}i'
        else:
            return f'{self.real} + {self.image}i'


n1 = Complex(2, 1)
n2 = Complex(5, 7)
print(n1)
print(n2)
n3 = n1 + n2
print(n3)
n4 = n1 * n2
print(n4)

# Проверка
a = 2 + 1j
b = 5 + 7j
print(a, b, sep='\n')
print(a + b)
print(a * b)
