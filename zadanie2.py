from math import sin, pi

# Проверка попадания точки в заштрихованную область
x = float(input("Введите x: "))
y = float(input("Введите y: "))

if 0 <= x <= pi and 0 <= y <= 0.5 and y <= sin(x) + 0.000000001:
    print("Точка принадлежит области")
else:
    print("Точка не принадлежит области")
