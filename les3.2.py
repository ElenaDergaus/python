# coding : utf-8
# lesson 3 exercise 2

# 2. Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения,
# город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.


def print_user_data(name, surname, year, city, phoneNumber, email):
    print(f'Имя: {name}; фамилия: {surname}; год рождения: {year}; город проживания: {city}; email: {email}; телефон: {phoneNumber}')

print_user_data(name = 'Иван', surname = "Иванов", year  = "1965", city = "Москва", phoneNumber = 1384598, email = 'ii@mail.ru')


# Ввод пользовательских данных
# userData = input("Введите через пробел ваши Имя, Фамилию, год рождения, город проживания, email, телефон: ").split()
# print_user_data(name = userData[0], surname = userData[1], year  = userData[2], city = userData[3], phoneNumber = userData[5], email = userData[4])



