#Напишите программу, принимающую на вход целое число, которая выводит True, если переданное значение попадает в интервал (−15,12]∪(14,17)∪[19,+∞) и False в противном случае (регистр символов имеет значение).

#Обратите внимание на разные скобки, используемые для обозначения интервалов. В задании используются полуоткрытые и открытые интервалы. Подробнее про это вы можете прочитать, например, на википедии (полуинтервал, промежуток).

#Sample Input 1:
#20
#Sample Output 1:
#True

#Sample Input 2:
#-20
#Sample Output 2:
#False

number = int(input())
if number > -15 and number <= 12 or number > 14 and number < 17 or number >= 19:
    print("True")
else:
    print("False")