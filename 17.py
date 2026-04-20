def check_divisor(x, d):
    if d * d > x:
        return 1
    
    if x % d == 0:
        return 0

    return check_divisor(x, d + 1)


def function1(x):
    if x < 2:
        return 0

    if x == 2:
        return 1

    return check_divisor(x, 2)


# Примеры использования
print(function1(7))   # Выведет 1 (простое)
print(function1(10))  # Выведет 0 (составное)
print(function1(1))   # Выведет 0 (не простое)
