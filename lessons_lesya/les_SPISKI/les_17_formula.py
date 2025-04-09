n = int(input())
list = []
result_list = []
for i in range(n):
    x = int(input())
    x1 = x**2 + 2 * x + 1
    list.append(x)
    result_list.append(x1)
print(*list, sep='\n')
print()
print(*result_list, sep='\n')

"""!! Важно! Python не понимает 2х и 2(х) - НУЖНО писать 2 * х"""

"""Вывод элементов списка, каждого на отдельной строке:

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(*numbers, sep='\n')
Приведённый выше код выводит:
"""