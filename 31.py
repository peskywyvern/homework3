line = input('Write smth here: ')
length = len(line)
if length < 7:
    print('Error')
else:
    center = length // 2
    new_line = line[center-1] + line[center] + line[center+1]
    print(new_line)
