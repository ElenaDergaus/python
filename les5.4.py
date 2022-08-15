# coding : utf-8
# lesson 5 exercise 4

# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При
# этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

numbers = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
content = []
with open("les5.4.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        a, b, c = line.split()
        aNew = numbers.get(a)
        content.append(" ".join([aNew, b, c]))

with open("les5.4-result.txt", 'w') as f_obj:
    for el in content:
        f_obj.write(el + "\n")
