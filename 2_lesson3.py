# 2-е задание урок 3
# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
#  имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры
#  как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.


def user_data(**kwargs):                   # Функция может принимать неопределённое число именованных параметров
                                         # переменная    **kwargs хранит словарь
    return f"Name: {kwargs['nme']}, Surname: {kwargs['snme']}, Year_Birth:{kwargs['ybirth']}," \
           f" City_of_res:{kwargs['cityres']}," \
           f" Email:{kwargs['eml']}, Phone:{kwargs['teln']}"


print(user_data(nme="Ivan", snme="Ivanov", ybirth= ' 1987', cityres= "Orel", eml= "plmnb@yandex.ru",
                teln= "+79874566789"))





