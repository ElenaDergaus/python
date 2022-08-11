# coding : utf-8
# lesson 3 exercise 1

# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def division(dividend, divider):
    if divider == 0:
        return "Деление на о!"
    else:
        res = dividend/divider
        return res


userNum1 = int(input("Введите делимое: "))
userNum2 = int(input("Введите делитель: "))

print(division(userNum1,userNum2))