def has_element(a, x):
    """Проверяет, содержится ли элемент 'x' в списке 'a' рекурсивным способом.
    """
    if len(a) == 0:
        return False

    if a[0] == x:
        return True

    return has_element(a[1:], x)


# Пример использования
numbers = [1, 5, 8, 12, 3]
print(has_element(numbers, 8))   # Выведет True
print(has_element(numbers, 10))  # Выведет False
