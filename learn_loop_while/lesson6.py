x = int(input('какой вклад сделан в рублях '))
y = int(input('сумма будет равна '))
p = int(input('под какой процент '))
# p = int(input('под какой процент ')) / 100  # 10 -> 0.1

year = 0
while x < y:
    x = int(x + (x * (p / 100)))
    # x = int(x + (x * p))
    year += 1

print("Количество лет:", year)

# TODO: Нужно самостоятельно разобрать!
