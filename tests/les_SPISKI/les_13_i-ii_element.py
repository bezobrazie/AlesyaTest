n = int(input()) # число строк
list = []
for i in range(n):
    stroka = input()
    len_stroka = len(stroka)
    list.append(stroka)
k = int(input()) # какой символ по счету
list_2 = []
for i in list:
    if len(i) >= k:
        list_2.append(i[k-1])
    else:
        continue
result = ''.join(list_2) # записывает элементы списка в строку
print(result)


"""if len_stroka > k:
    print(stroka.list[k])"""
   