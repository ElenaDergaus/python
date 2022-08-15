# coding : utf-8
# lesson 5 exercise 2

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить
# подсчёт строк и слов в каждой строке.

content = []
lineWords = []
with open("les5.2.txt") as f_obj:
    for line in f_obj:
        content.append(line.split())
        lineWords.append(len(content[-1]))

lineNum = str(len(content))

print(f"В файле {lineNum} строки.")
for i, el in enumerate(lineWords):
    print(f"Количество слов в {i+1}-й строке: {el}")
