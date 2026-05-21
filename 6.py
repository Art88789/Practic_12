def get_power_of_five(n):
    """Определяет, является ли число точной степенью 5, и возвращает показатель.
    """
    if n == 1:
        return 0

    if n < 5 or n % 5 != 0:
        return -1

    res = get_power_of_five(n // 5)

    if res == -1:
        return -1

    return 1 + res


# Примеры использования
print(get_power_of_five(125))  # Выведет 3 (5^3 = 125)
print(get_power_of_five(20))   # Выведет -1 (не степень 5)
print(get_power_of_five(1))    # Выведет 0 (5^0 = 1)
