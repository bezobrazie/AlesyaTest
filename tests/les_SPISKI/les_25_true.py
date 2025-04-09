fuel, weight, thrust = map(int, input().split()) 
pp = fuel + weight < thrust
pp == "True"
print(pp)






"""fuel — количество топлива (в тоннах),
weight — вес ракеты (в тоннах),
thrust — тяга двигателя (в тоннах)"""