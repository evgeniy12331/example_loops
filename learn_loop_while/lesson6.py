x = int(input('какой вклад сделан в рублях '))
y = int(input('сумма будет равна '))
p = int(input('под какой процент '))
i = 0
while x < y:
    x *= 1 +p/100
    i +=1
    print(i)