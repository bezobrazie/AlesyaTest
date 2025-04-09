n = int(input())
list = []
temp = 0
for i in range(n):
    x = int(input())
    x1 = temp + x
    list.append(x1)
    temp = x
    
del list[0]
print(list)