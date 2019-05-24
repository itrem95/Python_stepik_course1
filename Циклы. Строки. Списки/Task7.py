# Выведите таблицу размером n×n, заполненную числами от 1 до n2 по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5):
#
#
# ﻿
# Sample Input:
#
# 5
# Sample Output:
#
# 1 2 3 4 5
# 16 17 18 19 6
# 15 24 25 20 7
# 14 23 22 21 8
# 13 12 11 10 9

n = int(input())
table = [[0 for j in range(n)] for i in range(n)]

turns_counter = 0 # счётчик, отвечающий за поворот по часовой стрелке внутри таблицы
row = 0 # номер строки
col = 0 # номер столбца
for num in range(n**2):
    table[row][col] = num + 1
    if row == turns_counter+1 and col == turns_counter:
        turns_counter += 1
    if row == turns_counter and col < n - turns_counter - 1:
        col += 1
    elif col == n - turns_counter - 1 and row < n - turns_counter - 1:
        row += 1
    elif row == n - turns_counter - 1 and col > turns_counter:
        col -= 1
    elif col == turns_counter and row > turns_counter:
        row -= 1

for c in range(n):
    for d in range(n):
        print(table[c][d], end=" ")
    print()