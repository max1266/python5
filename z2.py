def summ(a,b):
    summ1 = a
    summ2 = a+b
    if summ1 == summ2:
        return summ1
    return summ(a +1, b -1)
a = int(input("Введите число: "))
b = int(input("Введите число: "))
print('Результат : ', summ(a,b))