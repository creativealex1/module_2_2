a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))
if a == b == c :
    print(3)
elif a == b or b == c or a == c :
    print (2)
elif a != b != c :
    print(0)
