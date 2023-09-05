# dept_summ = int(input('введите сумму долга '))
dept_summ = 100
print('василий ваша задолженность составляет', dept_summ, 'рублей')
money = int(input('сколько внесете денег '))

while money < dept_summ:
    print('мало , внесите еще')
    money = int(input('внесите еще '))
print('хватает')
