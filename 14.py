def print_reversed_digits(x):
    """Выводит в столбик все цифры числа 'x', начиная с конца, с помощью рекурсии.
    """
    print(x % 10)

    if x > 9:
        print_reversed_digits(x // 10)


# Пример использования
print_reversed_digits(123)
