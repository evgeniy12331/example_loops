hour = 0
all_task = 0
while True:
    hour += 1
    print('прошел',hour,'час')
    task = int(input('сколько задач решит максим '))
    all_task += task
    print('решено задач', all_task)
    call = int(input('звонит жена , взять трубку 1 - да, 0 - нет '))
    if call == 1:
        print('взять трубку ,зайти в магазин')
    if hour == 8:
        break
print('рабочий день окончен,')
