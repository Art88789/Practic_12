def odd_list(a, n):
    if n == 0:
        return []
    
    if a[0] % 2 == 0:
        return [a[0]] + odd_list(a[1:], n - 1)

    return odd_list(a[1:], n - 1)


# Пример использования
numbers = [1, 2, 3, 4, 5, 6]
print(odd_list(numbers, 6))  # Выведет [2, 4, 6]
