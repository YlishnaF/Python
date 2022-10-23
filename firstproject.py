#-----------------------------------Простые множители------------------------------
# def isSimpleNum(num):
#     k=2
#     while k!=num:
#         if(num%k==0):
#             return False
#         k+=1
        
#     return True   

# try:
#     num = int(input('Введите натуральное число '))
#     num>0
# except:
#     print('Неверно введено число!')
# if num==1:
#     print("Введено 1, 1 не является простым числом. Завершение программы")
# mas = []
# k=2
# while num!=1:
#     if(num%k==0):
#         if(isSimpleNum(k)):
#             mas.append(k)
#             num/=k
#     else:
#         k+=1
# print('Простые множители введеного числа: ', mas )
#------------------------------Неповторяющиеся элементы------------------------------
# from random import randint
# from unittest import result
# def masCreator(x):
#     mas=[[0] for i in range(x)]
    
#     for i in range(len(mas)):
#         mas[i]=randint(0, 9)
            
#     return mas

# mas=masCreator(10)
# print('Изначальный массив: ', mas)
# result=[]
# for i in range(len(mas)):
#     if(mas[i] in result):
#         continue
#     else:
#         result.append(mas[i])
# print('Уникальные элементы в массиве: ', result)

#------------------------------Корни квадратного уравнения------------------------------
# import re
# equation = input('Введите квадратное уравнение в виде: ax2+bx+c=0. Укажите все коэффициенты, даже если они равны 1 или 0: ')
# regex = re.compile(r'(-?\d+)x2([+-]\d+)x([+-]\d+)=0')
# matches = regex.match(equation)
# if matches is None:
#     print('Неверно введено уравнение')
#     exit()
# a = int(matches.group(1))
# b = int(matches.group(2))
# c = int(matches.group(3))
# D = b**2 - 4*a*c
# if(D>0):
#     x1=(-b + D**0.5)/(2*a)
#     x2=(-b - D**0.5)/(2*a)
#     print("Первый корень:  ", x1)
#     print("Второй корень:  ", x2)
# elif(D==0):
#      x1=-b+(D)**0.5/2*a
#      print("Один корень:  ", x1)
# else:
#     print('Корней нет')
# ---------------------------------------------Чат бот-------------------------------------------------
import json
from secrets import choice
data=[]

def save():
    with open("library.json", "w+", encoding="utf-8") as file:
        file.write(json.dumps(data, ensure_ascii=False))

try:
    with open("library.json", "r", encoding="utf-8") as file:
        data = json.load(file) 
except:
    data = {'Джоан Роулинг': ['Гарри Поттер и кубок огня', 'Гарри Поттер и тайная комната'], 'Лев Толстой':['Анна Каренина', 'Война и мир']}
    save() 
print(data)

print('Добро пожаловать, введите /start для начала работы ')
command = input()
if command=="/start":
    while True:    
        print('Введите /all для просмотра всей библиотеки,\n /author для просмотра всех книг автора и /exit для выхода')
        response = input('Введите команду ')
        if(response=='/all'):
            print(data)
        elif(response=="/author"):
            print('Введите имя автора из вашей библиотеки для просмотра всех его книг')
            author=input('Имя автора ')
            if(author not in data):
                print("У вас нет такого автора")
                continue
            print(data.get(author))
            print('Если вы хотите добавть книгу для данного автора, введите /append, \n/delete, ecли хотите ее удалить и /random для получения любой книги автора из библиотеки')
            command=input()
            if(command=='/append'):
                try:
                    command=input('Название книги ')
                    data[author].append(command)
                    print('Книга успешно добавлена, список книг автора: ', data.get(author))
                    save()
                except:
                    print('Нет такой книги в библиотеке')
            elif(command=='/delete'):
                try:
                    command=input('Название ')
                    data[author].remove(command)
                    print('Книга успешно улалена, список книг автора: ', data.get(author))
                    save()
                except:
                    print('Нет такой книги в библиотеке')
            elif(command=="/random"):
                print("Сегодня читаем прекраную книгу: ",choice(data.get(author)))
            
            else:
                print('Введена неверная комманда, попробуйте еще раз!')
        elif(response=="/exit"):
                print('Выходим их библиотеки, будем рады видеть вас снова!')
                exit()
else:
     print('Введена неверная комманда, попробуйте еще раз!')
