#Задание 3 урок 2
#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dic

try:
    season_list = [ 12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    season_dict = {'1': 12, '2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, '11': 10, '12':11 }
    a = 0
    while True:
        a = int(input('Ввеодите месяц года как целое число от 1 до 12 : '))
        if a < 13 and a > 0: break

    if season_list.index(a) < 3: print(f' Это зима !') # возвращает индекс первого вхождения указанного элемента  списка
    if season_list.index(a) > 8: print(f' Это осень !') # возвращает индекс первого вхождения указанного элемента  списк
    if season_list.index(a) > 2 and season_list.index(a) < 6: print(f' Это весна !')
    if season_list.index(a) > 5 and season_list.index(a) < 9: print(f' Это лето !')

    if season_dict[str(a)] < 3: print(f' Это зима ! ( словарь )')
    if season_dict[str(a)] > 8: print(f' Это осень ! ( словарь )')
    if season_dict[str(a)] > 2 and season_dict[str(a)] < 6: print(f' Это весна ! ( словарь )')
    if season_dict[str(a)] > 5 and season_dict[str(a)] < 9: print(f' Это лето ! ( словарь )')

except Exception:
    print('Ошибочный ввод данных !')


