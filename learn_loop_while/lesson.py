print('василий ваша задолженность составляет 100 рублей ')
dept_summ = int(input('введите сумму долга '))
money = int(input('сколько внесете денег'))
while money <= dept_summ:
    print('мало , внесите еще ')
    money = int(input('внесите еще'))
print('хватает')