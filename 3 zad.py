year = int(input("Введите год: "))

if (year % 4 == 0) and (year % 100 != 0):
    print("високосный")
else:
    print("нет")