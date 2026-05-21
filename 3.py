def get_arithmetic_element(a1, r, n):
    """Находит n-й член арифметической прогрессии рекурсивным способом.
    """
    if n == 1:
        return a1

    return get_arithmetic_element(a1, r, n - 1) + r


# Пример: первый член 5, разность 2, найти 10-й член
print(get_arithmetic_element(5, 2, 10))
