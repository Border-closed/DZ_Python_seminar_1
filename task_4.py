#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#Пример:
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21

xA=input('Введите х для А ')
yA=input('Введите y для А ')
xB=input('Введите х для B ')
yB=input('Введите y для B ')
try:
    xA=int(xA)
    yA=int(yA)
    xB=int(xB)
    yB=int(yB)
    import math
    d=round(math.sqrt((xB-xA)**2+(yB-yA)**2),3)
    print(d)
except:
    print('Вы ввели не число')