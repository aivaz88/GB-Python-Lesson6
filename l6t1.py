# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = input('Введите любое вещественное число: ')
# sum = 0
# for i in num:
#     if (i == '.' or i == ','):
#         next
#     else:
#         sum += int(i)
# print(sum)

num = input('Введите любое вещественное число: ')
list = [int(i) for i in num if i.isdigit()]
print(sum(list))