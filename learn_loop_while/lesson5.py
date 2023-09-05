flag = False
count_completed_task = 0
work_time = 8  # рабчих часов в день

print("Начался восьмичасовой рабочий день.")

i = 0
while count_completed_task <= work_time:
    print(str(i) + "-й час")

    task = int(input('Сколько задач решит Максим? '))
    call = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    count_completed_task += task

    if call != 0:
        flag = True

    i += 1

print("Рабочий день закончился. Всего выполнено задач:", count_completed_task)

if flag:
    print("Нужно зайти в магазин.")
