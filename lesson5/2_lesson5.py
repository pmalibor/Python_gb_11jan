# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк
# и слов в каждой строке.

my_f = open(".\dberr.txt", "r")    # открываем файл на чтение
                            # в котором записаны строки в переменную my_f.
                            # my_f.readlines - это список типа ['lkjlk', 'owiuoiu', 'kjhkjh', ], где элементы - строки
                            # из файла

print(f'Количество строк в фале: ', len(my_f.readlines()))  # с помощью функции len() подсчитываем число элементов в списке
my_f.close()                   # закрываем файл
my_f = open(".\dberr.txt", "r")
file_lines = my_f.readlines()
for line_num, line in enumerate(file_lines, 1):
    print(f'Количество слов в строке {line_num}:', len(line.split()))

my_f.close()                   # закрываем файл





