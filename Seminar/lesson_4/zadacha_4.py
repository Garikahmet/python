# Найдите корни квадратного уравнения двумя способами:
# 1. с помощью мат формул нахождения корней квдратного уравнения
# 2. с помощью доп библиотек пайтон

# with open('input.txt', 'r', encoding='utf-8') as file:
#     line = file.readline().split()
#     a, b, c = int(line[0]), int(line[1]), int(line[2])
#     d = b ** 2 - 4 * a * c
#     if d < 0:
#         print('Корней нет')
#     elif d == 0:
#         print(-b / 2 * a)
#     else:
#         print((-b + d ** 0.5) / 2 * a)
#         print((-b - d ** 0.5) / 2 * a)


"""terminal -> pip install sympy"""
a = 5
b = 1
c = 6
import sympy
x = sympy.Symbol('x')
print(sympy.solve(f'{a}* x ** 2 + {b} * x + {c}'))


import math
print(math.pi)