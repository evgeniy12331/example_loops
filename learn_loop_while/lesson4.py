# В старину, когда даже в столице билеты в общественном транспорте выдавали контролёры,
# существовало поверье:
# если на билете сумма первых трёх цифр в номере билета равна сумме последних трёх,
# то это к удаче.
#
# Напишите программу,
# которая получала бы на входе шестизначный номер билета
# и выводила, счастливый это билет или нет.
# К примеру, билеты 666 666 и 252 135 — счастливые,
# а 123 456 — нет.
# Подумайте, нужны ли для решения этой задачи циклы?

ticket = int(input('введите номер билета '))

six = ticket // 100_000  # разряд ста тысячи
five = ticket // 10_000 % 10  # разряд десяти тысячи
four = ticket // 1000 % 10  # разряд тысячи

three = ticket // 100 % 10
two = ticket // 10 % 10
one = ticket % 10

num1 = six + five + four
num2 = three + two + one

if num1 == num2:
    print('билет подходит ')
else:
    print('билет не подходит')
