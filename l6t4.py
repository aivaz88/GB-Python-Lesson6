#Напишите программу, которая принимает на вход координаты двух точек 
#и находит расстояние между ними в 2D пространстве.

# x1 = int(input('Введите координату Х первой точки: '))
# y1 = int(input('Введите координату Y первой точки: '))
# x2 = int(input('Введите координату Х второй точки: '))
# y2 = int(input('Введите координату Y второй точки: '))
# print(round(((x1-x2)**2+(y1-y2)**2)**0.5, 2))

def point():
    x = []
    x.append(int(input('Введите координату X: ')))
    x.append(int(input('Введите координату Y: ')))
    return x 

x1 = point()
x2 = point()
list1 = list(zip(x1, x2)) 
print(round(((list1[0][0]-list1[0][1])**2+(list1[1][0]-list1[1][1])**2)**0.5, 2))  