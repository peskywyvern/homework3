def func(a, b):
    if a == 10 or b == 10:
        return('True')
    elif a + b == 10:
        return('True')
    else:
        return('False')

x = int(input('First number: '))
y = int(input('Second number: '))
print(func(x, y))