# coding : utf-8
# lesson 3 exercise 7

# 7. Продолжить работу над заданием. В программу должна попадать строка из слов, разделённых пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Нужно сделать вывод исходной строки,
# но каждое слово должно начинаться с заглавной буквы. Используйте написанную ранее функцию int_func().


def int_func(text):
    newText = []
    for i in text:
        if not i.isalpha():
            print("Надо было ввести буквы!")
            quit()
        elif not i.islower():
            print("Надо было ввести буквы в нижнем регистре!")
            quit()
        else:
            i = i.title()
            newText.append(i)
    newText = " ".join(newText)
    return newText

userText = input("Введите несколько слов из маленьких латинских букв через пробел: ").split()
print(int_func(userText))