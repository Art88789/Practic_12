def get_max_index(a):
    """Находит индекс максимального элемента в списке рекурсивным способом.

    Если максимальных элементов несколько, возвращает индекс первого вхождения.
    """
    if len(a) == 1:
        return 0

    idx = get_max_index(a[1:])
    actual_idx = idx + 1

    if a[0] >= a[actual_idx]:
        return 0

    return actual_idx


# Пример использования
numbers = [3, 1, 7, 2, 5]
print(get_max_index(numbers))  # Выведет 2 (индекс числа 7)
