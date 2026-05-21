def get_combinations_count(n, k):
    """Вычисляет число сочетаний из n по k элементов рекурсивным способом.
    """
    if k == 0 or k == n:
        return 1

    if k > n:
        return 0

    return (
        get_combinations_count(n - 1, k - 1)
        + get_combinations_count(n - 1, k)
    )


# Пример использования: сочетание из 5 по 3 (равно 10)
print(get_combinations_count(5, 3))
