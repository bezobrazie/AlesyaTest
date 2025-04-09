n = int(input())
list = []
for i in range(n):
    stroka = input()
    list.append(stroka)
zapros = input()
for x in list:
    if zapros.lower() in x.lower(): # понижаем регистр запросу и элементам в списке
        print(x)
        


