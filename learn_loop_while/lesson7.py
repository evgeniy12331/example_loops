conceived_num = 7
guess_num = int(input('введите число '))
count = 0
while conceived_num != guess_num:
    count +=1
    if guess_num < conceived_num:
        print('число меньше')
    else:
        print('число больше ')
        guess_num = int(input('введите число '))
print('количество попыток ', count)
