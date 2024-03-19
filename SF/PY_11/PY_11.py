import pandas as pd
import numpy as np


# customer_df = pd.DataFrame({
#             'number': [0, 1, 2, 3, 4],
#             'cust_id': [128, 1201, 9832, 4392, 7472],
#             'cust_age': [13, 21, 19, 21, 60],
#             'cust_sale': [0, 0, 0.2, 0.15, 0.3],
#             'cust_year_birth': [2008, 2000, 2002, 2000, 1961],
#             'cust_order': [1400, 14142, 900, 1240, 8430]
#         })


# def delete_columns(df, col=[]):
#     set1 = set(col)
#     if set1.issubset(df.columns ):
#         new_df = df.drop(col, axis=1)
#         return new_df
#     else:
#         return None

# new_df = delete_columns(customer_df, col=['number','cust_yeadr_birth'])
# print(new_df )


# # На вход данной функции поступает строка с адресом.
# def get_street_type(address):
# # Создаём список географических пометок exclude_list.
#     exclude_list = ['N', 'S', 'W', 'E']
# # Метод split() разбивает строку на слова по пробелу.
# # В результате получаем список слов в строке и заносим его в переменную address_list.
#     address_list = address.split(' ')
# # Обрезаем список, оставляя в нём только последний элемент,
# # потенциальный подтип улицы, и заносим в переменную street_type.
#     street_type = address_list[-1]
# # Делаем проверку на то, что полученный подтип является географической пометкой.
# # Для этого проверяем его на наличие в списке exclude_list.
#     if street_type in exclude_list:
# # Если переменная street_type является географической пометкой,
# # переопределяем её на второй элемент с конца списка address_list.
#         street_type = address_list[-2]
# # Возвращаем переменную street_type, в которой хранится подтип улицы.
#     return street_type


# melb_data = pd.read_csv('C:/Users/aoreshkin.IT-ONE/VSProject/SF_DS_PYTHON/SF/PY_11/data/melb_data_ps.csv', sep=',')
# melb_df = melb_data.copy()


# test_series_1 = pd.Series([
#     'Опыт работы 8 лет 3 месяца',
#     'Опыт работы 3 года 5 месяцев',
#     'Опыт работы 1 год 9 месяцев',
#     'Опыт работы 3 месяца',
#     'Опыт работы 6 лет'
# ])

# test_series_2 = pd.Series([
#     'Опыт работы 5 лет',
#     'Опыт работы 5 месяцев',
#     'Опыт работы 1 год 1 месяц',
#     'Опыт работы 3 месяца',
#     'Опыт работы 7 лет'
# ])

# def get_experience(arg):
#     sp = arg.split()
#     if len(sp) > 4:
#         result = int(sp[2])*12 + int(sp[4])
#     else:
#         if len(sp[-1]) <= 4:
#             result = int(sp[2])*12
#         else:
#             result = int(sp[2])
#     return result



# print(test_series_1.apply(get_experience))

# from string import Template

# #Вершинина Татьяна Валентиновна ТС-23-07 08.12.23 Вариант 5
# #Задание №5
from math import* #Подключаем библиотеку
x = float(input('Введите вещественное число х =')) #вводим х
t = int(input('Введите целое число t =')) #вводим t
s = t//3 + 5 #считаем s
print ('Значение s = ', s) #выводим s
if t >= 0 and abs(x - s) - sqrt(t) > 0 and x > 0: #условие
    f = (log(x)/sqrt(abs(x - s) - sqrt(t))) #считаем f
    print('f = %3.f' % f) #выводим f
else: #иначе
    print('Значение f не определено') #выводим значение не определено