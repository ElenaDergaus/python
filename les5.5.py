# coding : utf-8
# lesson 5 exercise 5

# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

# Количество чисел, которые будут записаны в файл
numberCount = random.randint(1, 100)

# Формируем файл из рандомных чисел
with open("les5.5.txt", 'w') as f_obj:
    for i in range(numberCount):
        n = random.randint(1, 100)
        f_obj.write(str(n) + " ")

# Считываем получившиеся данные из файла, формируем из них список
with open("les5.5.txt", 'r') as f_obj:
    content = map(int, f_obj.read().split())

print(sum(content))