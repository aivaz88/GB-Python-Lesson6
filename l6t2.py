# Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# x = int(input('Введите число: '))
# if x == 6 or x == 7:
#     print('да')
# elif 0 < x < 6:
#     print('нет')
# else:
#     print('нет такого дня недели')

y = (lambda x: 5 < x < 8) (int(input('Введите число: ')))
if y: print('YES')
else: print('NO')
