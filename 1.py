def pownum(a, n):
    """Вычисляет результат возведения числа 'a' в целую степень 'n' рекурсивно.
    """
    if n == 0:
        return 1

    return a * pownum(a, n - 1)


# Пример использования
result = pownum(2.5, 3)
print(result)
