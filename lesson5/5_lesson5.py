# 5. Создать (программно) текстовый файл, записать в него программно набор чисел,
# разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

with open('file5.txt', 'w') as file_write:                  # открываем файл file5.txt на запись
    input_num_string = input('Введите числа через пробел: ')    # вводим числа через пробел и присваиваем эту
                                                                # строку input_num_string
    print(input_num_string, file=file_write)                    # выводим эту переменную input_num_string и записываем
                                                                # ее в файл file5.txt

# Программа подсчитывает сумму чисел в файле в выодит на экран

with open('file5.txt') as file:    # открываем файл file5.txt на чтение
    str_in_file = file.read().rstrip().split()  # освобождаем строку от символов справа и пробелов
    print(str_in_file)
    num_list = [int(num) for num in str_in_file if num.isdigit()] # создаем числовой список перебирая эл-ты строки
    print(num_list)
    print(sum(num_list))



