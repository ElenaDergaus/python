# coding : utf-8
# lesson 2 exercise 3

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и dict.

month = input("Введите номер месяца:")

# Через списки
winter = [1,2,12]
spring = [3,4,5]
summer = [6,7,8]
outumn = [9,10,11]

seasons = [winter,spring,summer,outumn]
txtSeasons = ['зима','весна','лето','осень']
for i in seasons:
    if int(month) in i:
        ind = seasons.index(i)
        print(txtSeasons[ind])



# Через dict

seasons = {"1": "зима", "2": "зима", "3": "весна", "4": "весна", "5": "весна", "6": "лето", "7": "лето", "8": "лето", "9": "осень", "10": "осень", "11": "осень", "12": "зима"}
print(seasons.get(month))

# Через dict 2
seasons = {"зима": (12, 1, 2), "весна": (3, 4, 5), "лето": (6, 7, 8), "осень": (9, 10, 11)}
month = int(month)

for i, j in seasons.items():
    if month in j:
        print(i)
