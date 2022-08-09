# coding : utf-8
# lesson 2 exercise 6

# 6. * Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.

productList = []
newProduct = ()
n = 0
keyList = ['Название', "Цена", "Количество", "Единица измерения"]
userDataList = []
flag = "Y"

while flag == "Y":
    userDataList.clear()
    print("Введите данные о товаре:")
    for i in range(len(keyList)):
        userDataList.append(input(f"{keyList[i]} товара: "))
    n += 1
    newData = dict(zip(keyList, userDataList))
    newProduct = (n, newData)

    productList.append(newProduct)
    print(newProduct)
    flag = input("Хотите ввести еще товар? Y/N")

# Нужно собрать аналитику о товарах. Реализовать словарь,
# в котором каждый ключ — характеристика товара, например, название.
# Тогда значение — список значений-характеристик, например, список названий товаров.

prodactAnalytics = {}

analiticsData = [[] for x in range(len(keyList))]

for i in range(len(productList)):
    for j in range(len(keyList)):
        analiticsData[j].append(productList[i][1].get(keyList[j]))

newData = dict(zip(keyList, analiticsData))
print(newData)

