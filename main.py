def GeneratorAB(lst, a, b):
    a = max(0, a)
    b = min(len(lst) - 1, b)

    for i in range(a, b + 1):
        print(lst[i])

lst = []
n = int(input("Введите количество элементов в списке: "))

for i in range(n):
    number = int(input(f"Введите число {i + 1}: "))
    lst.append(number)

a = int(input("Введите a: "))
b = int(input("Введите b: "))

GeneratorAB(lst, a, b)
