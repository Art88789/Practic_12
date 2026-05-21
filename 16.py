def get_hex_char(digit):
    """Возвращает символьное представление цифры для систем счисления до 16.
    """
    digits = "0123456789ABCDEF"
    return digits[digit]


def convert_from_decimal(x, n):
    """Переводит число из десятичной системы в систему счисления с основанием n.

    Использует рекурсивный алгоритм деления на основание системы.
    """
    if x < n:
        return get_hex_char(x)

    return convert_from_decimal(x // n, n) + get_hex_char(x % n)


# Примеры использования
print(convert_from_decimal(10, 2))   # Выведет "1010"
print(convert_from_decimal(255, 16)) # Выведет "FF"
print(convert_from_decimal(12, 8))   # Выведет "14"
