# -------------------------------------------Сумма всех чисел------------------------------------------------
# sum=0
# num=0
# try:
#     num=float(input("Введите число: "))
# except:
#     print('Необходимо ввести число, допущена ошибка!')
# while num %1!=0:   
#     num=round(num*10, 7)
# while num!=0:
#     sum+=(num%10)
#     num/=10
#     num=int(num)
# print('Сумма всех чисел = ', sum)

# -------------------------------------------Произведение чисел------------------------------------------------

# def castomMultiply(n):
#     mult=1
#     while n!=1:
#         mult*=n
#         n-=1
#     return mult

# num=0
# mas=[]
# try:
#     num = int(input('Введите целое положительное число: '))
# except:
#     print('Необходимо ввести целое положительное число, допущена ошибка!')    

# for i in range(1,num+1):  
#     mas.append(castomMultiply(i))
# print(mas)

# -------------------------------------------Поиск текста в тексте------------------------------------------------

# a=input('Введите строку, которую будем искать в тексте: ')
# b=input('Введите текст: ')
# mas=b.split(a)
# print('Количетва вхождений одной строки в другую: ', len(mas)-1)

# -----------------------------------------Расстояние между точками------------------------------------------------
# x=0
# try:
#     x=int(input('Введите колтчесво пространств: '))
# except:
#     print('Введено неверное значение!')    
# coordFirst = []
# coordSecond =[]
# print('Введите координаты первой точки')

# for i in range(x):
#     try:
#         coordFirst.append(int(input(f'Координата номер {i+1} ')))
#     except:
#         print('Неверно введено число')

# print('Введите координаты второй точки')

# for i in range(x):
#     try:
#         coordSecond.append(int(input(f'Координата номер {i+1} ')))
#     except:
#         print('Неверно введено число')
# diff = []
# result=0

# for i in range(x):
#     diff.append(int(coordSecond[i])-int(coordFirst[i]))
#     result+=diff[i]**2
# print('Расстояние между точками: ', result**0.5)

# -----------------------------------------Истина-----------------------------------------------

import random
import time

countPred = random.randint(5,25)
t = time.time()
for i in range(100):
    leftSide = random.choice([True, False])
    rightSide = not random.choice([True, False])
    for i in range(countPred-1):
        leftSide = leftSide or random.choice([True, False])
        rightSide = rightSide and not random.choice([True, False])

    resultPr = (not leftSide == rightSide)
t2 = time.time()
print('Время работы программы в сек: ', t2-t)