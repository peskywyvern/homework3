line = input('Write a line: ')
number = int(input('An index of word we wanna delete is: '))
print(line.replace(line[number], ''))
