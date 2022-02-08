# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных будет свидетельствовать пустая строка.

inp_string = input('Input the line will be added to the file1 : ')  # вводим строку которую добавим в file1

with open('File1', 'w') as file:  # открываем файл file1 на запись и создаем его если он не создан ранее
    while inp_string:             # пока строка введена начемаем цикл , если сторка не вводиться то inp_string == False
                                    # и цикл заканчивается
        file.write(inp_string+'\n')   # используем метод file.write для записи строки inp_string и символа перевода
                                        # строки '\n'
        inp_string = input('Input the next line will be added to the file1 or press  Enter to escape : ')





