# Печать целого числа

i = 234.567

print(int(i))
print(float(i))
print(3 + 8)

# Стринговая переменная

str = "Hi, there"

print(str)

# Булевая переменная
bool = False
print(not(bool))

# ИЗМЕНЯЕМАЯ коллекция объектов
list = ["Hi", 44.6, 332, "there"]
print(list[2])

# Кортеж - НЕизменяемая коллекция объектов
tuple = ("Hi world", 3.14, 8889)

print(tuple[0])

# Словарь - неизменяемая коллекция объектов с доступом по ключу

dict = {"a1": 223, "a2": 45, "name": "anton", "age": 33}

print(dict["a2"], dict["age"])

# Использовние input - всегда вывод строковый

str = input("Как ваше имя: ")
print(str)

# Использовние input для целых чисел

s = input("Введите целое число: ")
print(int(s))
