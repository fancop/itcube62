"Задача №4"

import math

# Ввод коэффициентов квадратного уравнения
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Вычисление дискриминанта
D = b**2 - 4*a*c

# Вычисление корней
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Корни уравнения: x1 =", x1, "и x2 =", x2)
elif D == 0:
    x = -b / (2*a)
    print("Уравнение имеет один корень: x =", x)
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print("Уравнение не имеет действительных корней. Комплексные корни: x1 =", real_part, "+", imaginary_part, "i и x2 =", real_part, "-", imaginary_part, "i")
