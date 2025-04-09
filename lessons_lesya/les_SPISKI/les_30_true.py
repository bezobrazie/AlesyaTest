# Считываем входные данные
money, outfit_ready, friends_going, feeling_good = input().split()

# Преобразуем значения в соответствующие типы
money = int(money)                     # Деньги Наташи
outfit_ready = outfit_ready == "True"  # Готов ли наряд
friends_going = friends_going == "True"  # Идут ли друзья
feeling_good = feeling_good == "True"  # Хорошо ли она себя чувствует
money = money >= 20
value = (money == outfit_ready == friends_going == feeling_good != False) or(money or outfit_ready or friends_going or feeling_good == True)
print(value)