n = 100 // 2

while True:
    print('число равно , больше или меньше ', n)
    answer = int(input('1 - равно , 2 - больше , 3 - меньше '))

    if answer == 1:
        print('угадали')
        break
    elif answer == 2:
        n += 1
    else:
        n -= 1
