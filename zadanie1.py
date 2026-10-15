# Вычисление выражения
a = float(input("Введите a: "))
b = float(input("Введите b: "))
f = float(input("Введите f: "))

if a == 0:
    print("Ошибка: a не должно быть равно нулю")
else:
    result = (a + b - f / a) + f * a * a - (a + b)
    print("Результат:", result)
