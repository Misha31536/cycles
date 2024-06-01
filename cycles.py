first = int(input("Ввведите первое число "))
second = int(input("Введите второе число "))
third = int(input("Введите третье число "))
quantity =int(1)
if first == second:
    quantity = quantity + 1
    if first == third:
        quantity = quantity +1
    print("одинаковых чисел ", quantity)
elif second == third:
    print("одинаковых чисел ", quantity + 1)
else:
    print("одинаковых чисел ", quantity -1)

