
entered_list = input("Введите числа последовательности через пробел: ").split()
num_list = list(map(int, entered_list))

num_set = set()

for num in num_list:
    if num in num_set:
        print(f"{num} - YES")
    else:
        print(f"{num} - NO")
        num_set.add(num)