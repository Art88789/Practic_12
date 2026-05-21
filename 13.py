def get_even_numbers(a, n):
    """Выбирает все чётные числа из первых 'n' элементов списка рекурсивно.
    """
    if n == 0:
        return []

    if a[0] % 2 == 0:
        return [a[0]] + get_even_numbers(a[1:], n - 1)

    return get_even_numbers(a[1:], n - 1)


# Пример использования
numbers = [1, 2, 3, 4, 5, 6]
print(get_even_numbers(numbers, 6))  # Выведет [2, 4, 6]
