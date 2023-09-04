pos_num = 0
neg_num = 0
number = int(input('введите число '))
while number !=0:
    if number > 0:
        pos_num +=1
    else:
        neg_num -=1
    number = int(input('введите число '))
print('количество положительных чисел',pos_num)
print('количество отрицательных чисел ', neg_num)