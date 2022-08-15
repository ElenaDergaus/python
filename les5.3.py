# coding : utf-8
# lesson 5 exercise 3


# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и
# величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее
# 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода
# сотрудников.


employees = {}

with open("salaries.txt", "r", encoding='utf-8') as f_obj:
    for line in f_obj:
        name, money = line.split()
        new_dict = {name: int(money)}
        employees.update(new_dict)


print("Менее 20000 р получают: ")
for i,el in employees.items():
    if el < 20000:
        print(i)

meanSalary = sum(employees.values())/len(employees)

print(f"Средняя зарплата: {meanSalary}")