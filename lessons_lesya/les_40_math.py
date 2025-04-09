import math
v = int(input())
ϴ = int(input())
ϴ = math.radians(ϴ)  
g = 9.81

T = (2 * v * math.sin(ϴ)) / g

H = (v**2) * ((math.sin(ϴ))** 2) / (2 * g)

R = (math.pow(v, 2) * math.sin(2 * ϴ) / g)

print(round(T, 2))
print(round(H, 2))
print(round(R, 2))

# https://stepik.org/lesson/1570443/step/16?unit=1591621










#print("\u03F4")