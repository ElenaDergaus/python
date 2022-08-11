# coding : utf-8
# lesson 3 exercise 6

# 6. Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(text):
    if not text.isalpha():
        print("Надо было ввести буквы!")
        quit()
    elif not text.islower():
        print("Надо было ввести буквы в нижнем регистре!")
        quit()
    else:
        text =text.title()
        return text

userText = input("Введите слово из маленьких латинских букв: ")
print(int_func(userText))
