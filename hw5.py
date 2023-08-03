# Задача 26: Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8 

# a = 3
# b = 5
# def f(a, b):
#     if (b == 1):
#         return (a)
#     if (b != 1):
#         return (a * f(a, b - 1))
# print(f(a, b))

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя
# *Пример:* 2 ; 2 ; 4
# a = 3
# b = 5
# def sum(a, b):
#   if b == 0:
#     return 0
#   return sum(a, b - 1) + 1
# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# return sum(a, b) + 1 - такое использовать нельзя
# *Пример:* 2 ; 2 ; 4

a = int(input('Введите 1-ое неотрицательное число: '))
b = int(input('Введите 2-ое неотрицательное число: '))
def recursive_summ(a, b):
    if a == 0:
        return b
    else:
        return recursive_summ(a -1, b + 1)
print(recursive_summ(a, b))