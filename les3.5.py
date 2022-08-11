# coding : utf-8
# lesson 3 exercise 5

# 5. Программа запрашивает у пользователя строку чисел, разделённых пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделённых пробелом и снова нажать Enter. Сумма вновь введённых чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введён после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.


flag = "Y"
generalSum = 0


def summa(numbers):
    """ Вызывает функцию проверки и считает сумму"""
    global flag
    flag, numbers = check_symbol(numbers)
    numbers = [int(i) for i in numbers]
    res = sum(numbers)
    return flag, res


def check_symbol(numbers):
    """Проверяет пользовательский ввод на наличие спецсимвола"""

    """Если найден спецсимвол, меняет флаг и делает срез
     из пользовательского ввода до спецсимвола
    """
    global flag
    for i in numbers:
        if not i.isdigit():
            ind = numbers.index(i)
            flag = "Q"
            numbers = numbers[:ind]
    return flag, numbers


while flag == "Y":
    userNumbers = input('Введите 3 числа через пробел: ').split()
    flag, locSum = summa(userNumbers)
    generalSum += locSum
    print(generalSum)

    if flag != "Y":
        quit()
    else:
        flag = input("Хотите ввести еще числа? Y/N")
