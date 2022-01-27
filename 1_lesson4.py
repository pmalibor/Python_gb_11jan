# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчёта заработной платы сотрудника. Используйте в нём формулу:
# (выработка в часах*ставка в час) + премия. Во время выполнения
# расчёта для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, productivity, rate_per_hour, bonus = argv
# Используем пример из методички, три параметра productivity, rate_per_hour, bonus
print("Имя скрипта: ", script_name)
print("Параметр 1: ", productivity)
print("Параметр 2: ", rate_per_hour)
print("Параметр 3: ", bonus)
print('Заработная плата : ', int(productivity) * int(rate_per_hour) + int(bonus))
