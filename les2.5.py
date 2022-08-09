# coding : utf-8
# lesson 2 exercise 5

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.


rating = [7, 5, 3, 3, 2]

insertFlag = "Y"

while insertFlag == "Y":
    newEl = int(input('Введите новый элемент рейтинга:'))
    if newEl > rating[0]:
        rating.insert(0, newEl)
    elif newEl < rating[-1]:
        rating.append(newEl)
    else:
        for ind, el in enumerate(rating):
            if el >= newEl > rating[ind + 1]:
                posInd = rating.index(el)
                rating.insert(posInd + 1, newEl)
                break

    print(rating)

    insertFlag = input("Хотите ввести еще один элемент? Y/N")


# Можете, пожалуйста подсказать, как можно решить данную задачу оптимальнее?
# Есть ощущение, что как-то можно