# coding : utf-8
# lesson 5 exercise 7

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая
# строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также
# среднюю прибыль. Если фирма получила убытки, в расчёт средней прибыли её не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а
# также словарь со средней прибылью. Если фирма получила убытки, также добавить её в
# словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджер контекста.

import json

keyList = []
profitList = []
n = 0
sumPr = 0

with open("les5.7.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        key, form, revenue, costs = line.split()
        keyList.append(key)
        profit = int(revenue)-int(costs)
        if profit >= 0:
            sumPr += profit
            n += 1
        profitList.append(profit)
    averageProfit = sumPr/n

thirstDict = dict(zip(keyList, profitList))
secondDict = {"average_profit": averageProfit}

Data = [thirstDict, secondDict]

with open("my_file.json", "w", encoding='utf-8') as write_f:
    json.dump(Data, write_f)
