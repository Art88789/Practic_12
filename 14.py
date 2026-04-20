def numbers(x):
    print(x % 10)

    if x > 9:
        numbers(x // 10)


# Пример использования
numbers(123)
