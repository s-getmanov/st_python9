#Запросим размер массива
N = int(input("Введите максимальное количество чисел: ")) 

while not (1 <= N and N <= 100000):
    print(f"Максимальное количество чисел должно быть в интервале 1 ≤ N ≤ 100000! Вы ввели {len(N)}!")
    N = int(input("Введите максимальное количество чисел: ")) 

work_list = []

# Обеспечим ввод строго нужного количества элеметов.
# Будем запрашивать ввод, пока не будет введено нужное количество элементов
while len(work_list) < N:
    ost = N - len(work_list)
    current_list = list(map(int, input(f"Введите {ost} чисел через пробел: ").split()))

    for i in current_list:
        # В рабочий список добавим только елементы, подходящие под условие задачи  
        if abs(i) >= 1 and abs(i)<= 2*10e9:
            work_list.append(i)            
        if len(work_list) == N:
            break    
result_set = set(work_list)

print(f"Количество различных чисел -  {len(result_set)} ")