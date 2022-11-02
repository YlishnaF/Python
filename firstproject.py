# ----------------------------------------------Игра с конфетами----------------------------------------------------
# import random
# import re
# from secrets import choice

# candies = 201
# print('Сыграем в короля конфет, сейчас узнаем, чей ход будет первым')
# hod = choice([1,2])
# if (hod==1):
#     print('Ваш первый ход')
# else:
#     print('Ходит искусственный интеллект Петя')  

# def botStep(candies):
#     if candies<=28:
#         return candies
#     elif candies<=57:
#         return candies-29
#     elif candies<=85:
#         return random.randint(1,candies-58)
#     else:
#         return random.randint(1,28)

# while (candies!=0):
#     print('Осталось ', candies, ' конфет')
#     if(hod%2!=0):
#         hod+=1
#         amount=0
#         notAcceptAnswer=True
#         while (notAcceptAnswer):
#             try:
#                 amount = int(input('Введите количество конфет, которое хотите забрать: '))
#             except:
#                 print('')
#             if (candies-amount)>0 and amount<29 and amount!=0:
#                 notAcceptAnswer=False
#             else:                
#                 print('Неверное количество конфет или не число, можно взять от 1 до 28 конфеты, но не больше, чем лежит на столе, попробуйте еще раз')
#                 continue
#         candies-=amount        
#         if(candies==0):
#             print('Вы победили бота!')
#     else:
#         hod+=1
#         botAmount = botStep(candies)
#         candies-=botAmount
#         print('Петя взял ', botAmount, ' конфет')
#         if(candies==0):
#             print('Исскусивенный интеллект победил!')
# ---------------------------------------------- RLE алгоритм----------------------------------------------------
# import re

# def codingFile(fromPath, toPath):
#     data=open(fromPath, 'r', encoding="utf-8")
#     dataTo=open(toPath, 'w', encoding="utf-8")
#     res =[]
#     for line in data:
#         res.append(line)
#     k=1
#     for i in range(len(res)):
#         arr=list(res[i])
#         ch =arr[i]
#         for j in range(1, len(arr)):
#             if(arr[j]==ch): k+=1
#             else: 
#                 dataTo.write(str(k)+ch)
#                 ch=arr[j]
#                 k=1
#         dataTo.write(str(k)+ch)

# codingFile('file.txt','result.txt')

# def decording(pathFrom, pathTo):
#     regex = re.compile(r'(\d+[a-zA-Z\n])')
#     data=open(pathFrom, 'r', encoding="utf-8")
#     dataTo=open(pathTo, 'w', encoding="utf-8")
#     res =[]
#     for line in data:
#         res.append(line)
#     k=1
#     for i in range(len(res)):
#         matches =regex.findall(res[i])
#         for j in range(len(matches)):
#             arr = [list(matches[j])[len(matches[j])-1] for k in range (int(matches[j][:-1]))]
#             for n  in range(len(arr)):
#                 dataTo.write(arr[n])

#     dataTo.close
#     data.close

# decording('result.txt','file.txt')

# ----------------------------------------------Удалить слова----------------------------------------------------
# import re
# text ='aбввап aапбв aбв впварпа вапы'
# words = text.split()
# for word in words:
#     if('aбв' in word):
#         words.remove(word)
# print('Из строки: ',text, ' удалили слова, которые содержат абв, в результате получили: ', ' '.join(words))

# ----------------------------------------------Сумма квадратного уравнения----------------------------------------------------
# например, 5*x^3 + 2*x^2 + 6 и 7*x^2+6*x+3 , Тогда их сумма будет равна 5*x^3 + 9*x^2 + 6*x + 9
import re
l1='5x3-2x2-6'
l2='-87x2-16x+3'
dic ={}

def createMap(equation):
    regex = re.compile(r'(-?\d+)x+')
    regex2 = re.compile(r'(x-?\d)')
    regex3=re.compile(r'(-?\d)$')
    matches = regex.findall(equation)
    matches2 = regex2.findall(equation)
    matches3 = regex3.findall(equation)
    if (len(matches)-len(matches2))==1:
        if('x') in dic: 
            dic['x']=int(matches[len(matches)-1])+int(dic['x'])
        else:
            dic['x']=int(matches[len(matches)-1])
    for i in range (len(matches2)):
        if(matches2[i]) in dic:
            dic[matches2[i]]=int(matches[i])+int(dic[matches2[i]])
        else:
            dic[matches2[i]]=int(matches[i])
    if len(matches3)!=0:
        if('0' in dic):
            dic['0']=int(matches3[0])+int(dic['0'])
        else:
            dic['0']=int(matches3[0])

createMap(l1)
createMap(l2)

sorted_dic = dict(sorted(dic.items(),reverse=True))
result=''
for key, value in sorted_dic.items():
    if(key=='0'):
        if(value>0):    
            result=result+"+"+str(value)
            continue
        else:
            result=result+str(value)
            continue

    if(value>0):    
        result=result+"+"+str(value)+key
    else:
        result=result+str(value)+key
if(result.startswith('+')):
    result = result.replace('+', '', 1) 
print("Cуммой уравнений {} и {} является {}".format(l1,l2, result))
