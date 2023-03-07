def summ(a, b):
    if (b == 1):
        return a
    if (b != 1):
        return (a * summ(a, b - 1))
a = int(input("Введите число: "))
b = int(input("Введите его степень: "))
print("Результат возведения в степень равен:", summ(a, b))
