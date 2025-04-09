n = int(input())
list = []
for i in range(n):
    stroka = input()
    list.append(stroka)
my_list = dict.fromkeys(list)
print(*my_list, sep='\n')


#list = list(dict.fromkeys(list))
#key = my_list(dict.keys(my_list))
#for key in my_list.keys():