n = int(input())
jj = []
for i in range(n):
    chisla = int(input())** 3
    jj.append(chisla)
print(list(jj))

"""На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу, которая создаёт из указанных чисел список их кубов, а затем выводит его

Sample Input 1:

5
1
2
3
4
5
Sample Output 1:

[1, 8, 27, 64, 125]"""