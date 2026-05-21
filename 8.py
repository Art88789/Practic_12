def get_fibonacci_number(k):
    """Находит k-й член последовательности Фибоначчи рекурсивным способом.
    """
    if k == 1 or k == 2:
        return 1

    return get_fibonacci_number(k - 1) + get_fibonacci_number(k - 2)


# Пример: 7-й член последовательности Фибоначчи (1, 1, 2, 3, 5, 8, 13)
print(get_fibonacci_number(7))
