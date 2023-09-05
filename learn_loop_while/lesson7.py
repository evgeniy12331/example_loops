conceived_num = 7  # загаданное число

count = 0
while conceived_num != (guess_num := int(input('введите число '))):
    count += 1

    if guess_num < conceived_num:
        print('число меньше')
    else:
        print('число больше ')

print('количество попыток', count)
