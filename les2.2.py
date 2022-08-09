# coding : utf-8
# lesson 2 exercise 2

# 2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

userList = input("Введите любое количество чисел:").split()
lenList = len(userList)

if lenList == 0:
    print("Вы ничвего не ввели!")
    quit()

n = lenList if lenList % 2 == 0 else (lenList-1)

for i in range(0,n,2):
    userList[i],userList[i+1] = userList[i+1],userList[i]

print(userList)