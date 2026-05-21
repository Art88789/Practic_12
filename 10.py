def get_max_element(a):
    """Находит максимальный элемент в списке рекурсивным способом.
    """
    if len(a) == 1:
        return a[0]

    max_of_rest = get_max_element(a[1:])

    if a[0] > max_of_rest:
        return a[0]

    return max_of_rest


# Пример использования
numbers = [3, 1, 7, 2, 5]
print(get_max_element(numbers))
