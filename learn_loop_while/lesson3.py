total_even = 0
while (number := int(input('введите число '))) != 0:
    if number % 2 == 0:
        total_even += 1
print('количество четных чисел', total_even)
