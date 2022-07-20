# 1. задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.



# def fillArrayRandom(size: int, startNumber: int, endNumber: int)
#     array = []
#     for i in range(size):
#         array.append(random. randrange(startNumber, endNumber))
#     return array

# def fillArrayRandom(size: int):
#     array = []
# #     for i in range(size):
# #         array.append(random. randrange(-20, 21))
# #     return array

# import random
# size = int(input('Введите число '))
# array = ['12asdas331asdasd2', '543', '74', '243']

# print (array)

# number = input('Какое число ')
# a = False
# for i in array:
#     if (number in i):
#         a = True
# if(a):
#     print(f'{number} есть в {array}')
# else:
#     print('нет числа такого')

# 1. Задайте список. Напишите программу, которая определит, присутствует
# ли в заданном списке строк некое число.

# list = ['123', '321', '456', '96']
# count = '3'
# array_find = []

# for find_count in list:
#     if count in find_count:
#         array_find.append(find_count)
# print(array_find)




# 2. напишите программу, кот определит позицию 
# второго вхождения строки в списке либо сообщит, что ее нет

#*Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

# list = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# find = "qwe"
# index = -1
# for i in range (len(list)):  # i сам элемент, читается: для элемента в списке
#     if(list[i] == find):
#         index = i
# print(f'число вхождений = {index}')



# 3. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел

import time
def current_milli_time():
    return round(time.time())

#print(current_milli_time()%100)

number = int(input('size'))
tmp = 1
array = []
for i in range (number + 1 // 3):
    array.append(tmp * current_milli_time() // 100)
    array.append((tmp * current_milli_time() // 100) // 3)
    array.append((tmp * current_milli_time() // 100) // 100)
    tmp +=2
print(array)