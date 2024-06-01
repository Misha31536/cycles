first = int(input("Ввведите первое число "))
second = int(input("Введите второе число "))
third = int(input("Введите третье число "))
quantity =int(1)
if first == second and first == third:
    print("одинаковых чисел 3")
elif second == third or first == third or first == second:
    print("одинаковых чисел 2")
else:
    print("одинаковых чисел 0")

