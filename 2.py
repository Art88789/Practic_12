def count_digits(n):
    """Считает количество цифр в числе рекурсивным способом.
    """
    if n < 10:
        return 1

    return 1 + count_digits(n // 10)


# Пример использования
result = count_digits(12345)
print(result)
