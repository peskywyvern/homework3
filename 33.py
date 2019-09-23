def reverse(num):
    rev = 0
    initial_number = num;
    while num > 0:
        s = num % 10
        rev = rev*10 + s
        num = num // 10
    if rev == initial_number:
        return('True')
    else:
        return('False')

number = int(input('Write a number: '))
print(reverse(number))
