# coding : utf-8
# lesson 4 exercise 1

# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной
# платы сотрудника. Используйте в нём формулу: (выработка в часах*ставка в час) + премия. Во
# время выполнения расчёта для конкретных значений необходимо запускать скрипт с
# параметрами.

from sys import argv
script_name, production, wageRate, premium = argv

def salary(production, wageRate, premium):

    res = int(production) * int(wageRate) + int(premium)
    return res
print(salary(production, wageRate, premium))



