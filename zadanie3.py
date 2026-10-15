# Определение вида треугольника по углам
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a < 0 or b < 0 or c < 0:
    print("Стороны не могут быть отрицательными")
elif a + b < c or a + c < b or b + c < a:
    print("Треугольник с такими сторонами не существует")
elif a == 0 or b == 0 or c == 0 or a + b == c or a + c == b or b + c == a:
    print("Вырожденный треугольник: площадь равна нулю")
else:
    # Находим самую длинную сторону
    if a >= b and a >= c:
        difference = a * a - (b * b + c * c)
    elif b >= a and b >= c:
        difference = b * b - (a * a + c * c)
    else:
        difference = c * c - (a * a + b * b)

    if abs(difference) < 0.000000001:
        print("Прямоугольный треугольник")
    elif difference > 0:
        print("Тупоугольный треугольник")
    else:
        print("Остроугольный треугольник")
