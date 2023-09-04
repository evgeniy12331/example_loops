number = int(input('введите число '))
even_num = 0
while number!=0:
    number = int(input('введите число '))
    if even_num % 2==0:
        even_num +=1
print('количество четных чисел', even_num)
