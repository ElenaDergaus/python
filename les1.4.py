# coding : utf-8
# lesson 1 exercise 4
userNumber =int(input("Введите целое положительное число:"))
# Вариант 1
# if userNumber < 0:
#     print("Вы ввели отрицательное число")
#     quit()
# b = str(userNumber)
# len_b = len(b)
# maxNumber = 0
# i=0
# while i < len_b:
#     tmp = int(b[i])
#     if tmp>maxNumber:
#         maxNumber = tmp
#     i+=1
#
# print("Самое большое число: ", maxNumber)
# input()



#Вариант 2
if userNumber < 0:
    print("Вы ввели отрицательное число")
    quit()

remainder = userNumber % 1
dozens = 1
b = userNumber//dozens

maxDigit = 0
while b != 0:
    dozens *= 10
    remainder = userNumber % dozens
    userNumber -= remainder
    digit = remainder//(dozens/10)
    if maxDigit < digit:
        maxDigit = digit
    b = userNumber//dozens

print('Самое большое число: ', int(maxDigit))
