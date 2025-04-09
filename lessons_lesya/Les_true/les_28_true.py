# Считываем входные данные в одну строку
data_volume, cpu_load, memory, server_connection = input().split()

# Преобразуем данные в соответствующие типы
data_volume = float(data_volume)         # Объём данных (ТБ)
cpu_load = float(cpu_load)                 # Загрузка процессора (%)
memory = float(memory)                     # Доступная память (ГБ)
server_connection = server_connection == "True"  # Наличие соединения
volum = data_volume <= 1.0
cpu = cpu_load <= 70
mem = memory >= 16
value = volum == cpu == mem == server_connection == True
print(value)
