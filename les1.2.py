# coding : utf-8
# lesson 1 exercise 2

timeInSec = int(input("Введите время в секундах:"))

hours = timeInSec//3600
minutes = timeInSec//60 - hours*60
sec = timeInSec%60

if hours < 10:
    hours = str(hours)
    hours = '0'+hours
if minutes < 10:
    minutes = str(minutes)
    minutes = '0'+minutes
if sec < 10:
    sec = str(sec)
    sec = '0'+sec


print(f"{hours}:{minutes}:{sec}")