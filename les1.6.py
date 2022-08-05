# coding : utf-8
# lesson 1 exercise 6
proceeds =int(input("Введите значение выручки:"))
costs = int(input('Введите значение издержек:'))

if proceeds>costs:
    print("Фирма работает с прибылью")
    rent = (proceeds-costs)/proceeds
    print ("Рентабельность:", rent)
    employeesQ = int(input("Введите количество сотрудников в фирме:"))
    empProfit = (proceeds-costs)/employeesQ
    print("Прибыль фирмы в расчёте на одного сотрудника:", int(empProfit))
elif proceeds < costs:
    print("Фирма работает в убыток")
else:
    print("Фирма работает в 0")



