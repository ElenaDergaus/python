# coding : utf-8
# lesson 3 exercise 3

# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.


def my_func(num1, num2, num3):
    numbers = [num1, num2, num3]
    res = sum(numbers) - min(numbers)
    return res


userNum1, userNum2, userNum3 = [int(s) for s in input('Введите 3 числа через пробел: ').split()]

print(my_func(userNum1, userNum2, userNum3))
