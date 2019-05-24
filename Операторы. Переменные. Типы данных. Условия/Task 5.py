# Напишите программу, которая получает на вход три целых числа, по одному числу в строке, и выводит на консоль в три строки сначала максимальное, потом минимальное, после чего оставшееся число.
#
# На ввод могут подаваться и повторяющиеся числа.
#
# Sample Input 1:
#
# 8
# 2
# 14
# Sample Output 1:
#
# 14
# 2
# 8
# Sample Input 2:
#
# 23
# 23
# 21
# Sample Output 2:
#
# 23
# 21
# 23

number1, number2, number3 = int(input()), int(input()), int(input())

if number1 < number2:
    number1, number2 = number2, number1
if number1 < number3:
    number1, number3 = number3, number1
if number2 > number3:
    number2, number3 = number3, number2
print(number1) #max
print(number2) #min
print(number3) #the remaining number