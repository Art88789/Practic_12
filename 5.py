def get_remainder(a, b):
    """Вычисляет остаток от деления числа 'a' на 'b' рекурсивным вычитанием.
    """
    if a < b:
        return a

    return get_remainder(a - b, b)


# Пример использования: 17 разделить на 5, остаток 2
print(get_remainder(17, 5))
