# coding : utf-8
# lesson 1 exercise 5
proceeds =int(input("Введите значение выручки:"))
costs = int(input('Введите значение издержек:'))

if proceeds>costs:
    print("Фирма работает с прибылью")
elif proceeds<costs:
    print("Фирма работает в убыток")
else:
    print("Фирма работает в 0")



