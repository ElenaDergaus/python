# coding : utf-8
# lesson 5 exercise 1

# 1. Создать программный файл в текстовом формате, записать в него построчно данные,
# вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая
# строка.

content = input("Введите денные: ")
with open("text.txt", "w") as f_obj:
    while content:
        f_obj.write(content+"\n")
        content = input("Введите денные: ")


# Проверка
with open("text.txt") as f_obj:
    for line in f_obj:
        print(line)
