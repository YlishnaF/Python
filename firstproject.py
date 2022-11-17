#                       Крестики-нолики
# import random
# pole = [[".",".","."],[".",".","."],[".",".","."]]
# availableStep = ['00', '01', '02', '10','11','12','20','21','22']
# winCombinationsHuman =  [['00','01','02'], ['10','11','12'],['20','21','22'],['00', '10','20'],['01','11','21'],['02','12','22'],['00','11','22'],['02','11','20']]
# winCombinationsBot =  [['00','01','02'], ['10','11','12'],['20','21','22'],['00', '10','20'],['01','11','21'],['02','12','22'],['00','11','22'],['02','11','20']]

# def checkWin(hod):
#     if(hod==0):
#         if list(filter(lambda x: len(x)==0, winCombinationsHuman)):
#             print('Вы выйграли!')
#             exit()
#     elif(hod==1):
#         if list(filter(lambda x: len(x)==0, winCombinationsBot)):
#             print('Бот победил!')
#             exit()

# def printPole(mas):
#     for i in range(len(mas)):
#         for j in range(len(mas[i])):
#             print(mas[i][j], " ", end="")
#         print('\n', end="")

# def removeInComb(comb, s):
#     for i in range(len(comb)):
#         mas = list(filter(lambda x: x!=s, comb[i]))
#         comb[i] = mas

# def botStep():
#     step=False
#     win = list(filter(lambda x: len(x)==1, winCombinationsBot))
#     if(len(win)>0):
#         for i in range(len(win)):
#             for j in range(len(win[i])):
#                 if(win[i][j] in availableStep):
#                     step=True
#                     pole[int(list(win[i][j])[0])][int(list(win[i][j])[1])]='o'
#                     removeInComb(winCombinationsBot, win[i][j])
#                     availableStep.remove(win[i][j])
#     if(step==False):
#         winCombinationsHuman.sort(key=len)          
#         for i in range(len(winCombinationsHuman)):
#             for j in range(len(winCombinationsHuman[i])):
#                 if(winCombinationsHuman[i][j] in availableStep):
#                     pole[int(list(winCombinationsHuman[i][j])[0])][int(list(winCombinationsHuman[i][j])[1])]='o'
#                     removeInComb(winCombinationsBot, winCombinationsHuman[i][j])
#                     availableStep.remove(winCombinationsHuman[i][j])
#                     return

# hod=random.choice([0,1])

# while(True):
#     if(len(availableStep)==0):
#         print('Ничья')
#         exit()
#     if hod==0:
#         print('Ваш ход')
#         k = input('Введите координаты поля в формате 01, где 0 - координата по оси x, 1 - координата по оси y ')
#         if(k in availableStep):
#             pole[int(list(k)[0])][int(list(k)[1])]='x'
#             availableStep.remove(k)
#             removeInComb(winCombinationsHuman, k)
#             printPole(pole)
#             checkWin(hod)
#             hod=1
#     elif hod==1:
#         print('Ходит бот')
#         botStep()
#         printPole(pole)
#         checkWin(hod)
#         hod=0

#                               Калькулятор
import re

actions = {
  "*": lambda x, y: str(int(x) * int(y)),
  "/": lambda x, y: str(int(x) / int(y)),
  "+": lambda x, y: str(int(x) + int(y)),
  "-": lambda x, y: str(int(x) - int(y))
}

firstExpReg = r"\((.+?)\)"
symbol=r"(?!^)[\*\\\+\-]"
r = r"-?\d+[\*\\\+\-]-?\d+"

exp = "5*(2-9)+6"
match2 = re.findall(firstExpReg,exp)
for i in range(len(match2)):
    s=re.findall(symbol, match2[i])
    calc=actions.get(s[0])
    exp= exp.replace(match2[i], calc(match2[i].split(s[0])[0], match2[i].split(s[0])[1]))
exp=exp.replace('(','').replace(')','')

while(re.search(symbol,exp)!=None):
    match=re.findall(r,exp)
    for i in range(len(match)):
        s=re.findall(symbol, match[i])
        calc=actions.get(s[0])
        exp= exp.replace(match[i], calc(match[i].split(s[0])[0], match[i].split(s[0])[1]))

print('результат вычислений уравнения 5*(2-9)+6:',exp)