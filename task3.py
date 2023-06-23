# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


import fractions
print("Пример ввода 1/3, 1/52 и т.д")
a, b = input("Введите дробь: ").split("/")
c, d = input("Введите дробь: ").split("/")
print(f'умножение даст {int(a) * int(c)}/{int(b) * int(d)}')
print(f'сложение даст {int(a) + int(c)}/{int(b) + int(d)}')



# a = int(input("Введите числа: "))
# b = int(input("Введите числа: "))
# c = int(input("Введите числа: "))
# d = int(input("Введите числа: "))
# f1 = fractions.Fraction(a, b)
# print(f1)
# f2 = fractions.Fraction(c, d)
# print(f2)
# print(f1 + f2)