def search(a, x):
    if len(a) == 0:
        return 0
    
    if a[0] == x:
        return 1
    
    return search(a[1:], x)


# Пример использования
numbers = [1, 5, 8, 12, 3]
print(search(numbers, 8))   # Выведет 1
print(search(numbers, 10))  # Выведет 0
