def check_divisor(x, d):
    """Рекурсивно проверяет, делится ли число 'x' на делитель 'd'.

    Продолжает проверку, увеличивая 'd' на 1, пока d * d не станет больше x.
    """
    if d * d > x:
        return True

    if x % d == 0:
        return False

    return check_divisor(x, d + 1)


def is_prime(x):
    """Определяет, является ли целое число 'x' простым.
    """
    if x < 2:
        return False

    if x == 2:
        return True

    return check_divisor(x, 2)


# Примеры использования
print(is_prime(7))   # Выведет True (простое)
print(is_prime(10))  # Выведет False (составное)
print(is_prime(1))   # Выведет False (не простое)
