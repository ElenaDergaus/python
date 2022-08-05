# coding : utf-8
# lesson 1 exercise 3
userNumber =int(input("Введите целое положительное число:"))

dozen = userNumber+userNumber*10
hundred = dozen + userNumber*100
result = userNumber+dozen+hundred

print("Результат: ", result)
input()