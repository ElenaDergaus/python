# coding : utf-8
# lesson 4 exercise 5

# 5. Реализовать формирование списка, используя функцию range() и возможности генератора. В
# список должны войти чётные числа от 100 до 1000 (включая границы). Нужно получить
# результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

from functools import reduce

myList = [el for el in range(100, 1001) if el % 2 == 0]
resalt = reduce(lambda x, y: x+y, myList)
print(resalt)