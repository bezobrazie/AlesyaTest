a, b = map(int, input().split()) 
b_1 = 123 // 100 # вычисляем 1
b_2 = (123 // 10) % 10 # Вычисляем 2 (второе число)
b_3 = 123 % 10 # вчисляем 3
sum_b = (b_1 + b_2 + b_3)
vv = a % sum_b == 0 # если верно- True
vv == "True" #сравниваем , получили ли в vv - True, если нет- выведет -False
print(vv)


"""scores = list(map(int, input().split()))
pp = sum(scores)
print(pp)
"""
