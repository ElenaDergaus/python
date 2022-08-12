# coding : utf-8
# lesson 4 exercise 3

# 3. Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну
# строку.
# Подсказка: используйте функцию range() и генератор.


newList = [el for el in range(20, 240) if el % 20 == 0 or el % 21 == 0]
print(newList)