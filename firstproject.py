#------------------------------------------------------день недели----------------------------------------------------------------------
# def name(a):
#     if a>0 and a<8:
#         if a==1:
#             return'понедельник'
#         elif a==2:
#             return('вторник')
#         elif a==3:
#             return('среда')
#         elif a==4:
#             return('четверг')
#         elif a==5:
#             return('пятница')
#         elif a==6:
#             return('суббота')
#         else:
#             return('воскресенье')
#     else:
#         print('вне диапазона')  

# try:
#     a=int(input('Введите число: '))
#     print(name(a))
# except:
#     print('не является числом')

#-------------------------------------------------------проверка истинности-------------------------------------------------------------
# for x in True, False:
#     for y in True, False: 
#         for z in True, False:
#                 print(not (x or y or z) == (not x and not y and not z))                

#-------------------------------------------------------определение четверти-------------------------------------------------------------
# try:
#     x=int(input('введите первое число: '))
#     y=int(input('введите первое число: '))
# except:
#     print('неверные значения')

# if(x!=0 and y!=0):
#     if(x>0 and y>0):
#         print('1я четверть')
#     elif(x>0 and y<0):
#         print('4я четверть')   
#     elif(x<0 and y<0):
#         print('3я четверть')   
#     elif(x<0 and y>0):
#         print('2я четверть')   
# else:
#     print('числа не должны равняться 0!')



from ast import operator
from re import L

#----------------------------------------------------------------калькулятор--------------------------------------------------

# def calculator(a, oper, b):    
#     if oper=='+':
#         return (a+b)
#     elif oper=='-':
#         return (a-b)
#     elif oper=='/':
#         if b==0:
#             print('На 0 делить нельзя')
#             return
#         else:
#             return (a/b)
#     elif oper=='*':
#         return (a*b)   
#     elif oper=='pow':
#         return (a**b)   
#     elif oper=='mod':
#         return (a%b)  
#     else: 
#         print('Неверная операция ')
#         return        

# try:
#     a=float(input('a= '))
#     oper = input('Введите операцию: ')
#     b=float(input('b= '))
# except: 
#     print('Введено неверное число')
# print(calculator(a,oper, b))

#---------------------------------------------------------сортировка массива----------------------------------------------------------         
from random import randint

def sort(list):  
    for i in range(0, len(list)-1):
        for j in range(0, len(list)-1):
            if list[j]>list[j+1]:
                a=list[j]
                list[j] = list[j+1]
                list[j+1] = a
    

def masCreator(x,y):
    mas=[[0]*y for i in range(x)]
    
    for i in range(len(mas)):
        for j in range(len(mas[i])):            
            mas[i][j]=randint(0, 15)
            
    return mas

try:
    x=int(input('Количество строк в массиве '))
    y=int(input('Количество столбцов в массиве '))
except:
    print('не является числом')

mas=masCreator(x,y)
print('Изначальный массив ',mas)
listSort = []

for i in range (len(mas)): 
      for j in range ( len(mas[i]) ): 
        listSort.append(mas[i][j])        
       
sort(listSort)

k=0

for i in range (x):
    for j in range (y): 
        mas[i][j]=listSort[k]
        k+=1
print('Отсортированный массив ', mas)


