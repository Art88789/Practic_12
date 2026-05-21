def convert_to_binary(x):
    """Переводит целое неотрицательное число из десятичной системы в двоичную.

    Использует рекурсивный метод деления на 2.
    """
    if x < 2:
        return str(x)

    return convert_to_binary(x // 2) + str(x % 2)


# Пример использования
print(convert_to_binary(10))  # Выведет "1010"
print(convert_to_binary(25))  # Выведет "11001"
