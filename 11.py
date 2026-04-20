def ind_maxlist(a):
    if len(a) == 1:
        return 0
    
    idx = ind_maxlist(a[1:])
    actual_idx = idx + 1
    
    if a[0] >= a[actual_idx]:
        return 0
    
    return actual_idx


# Пример использования
numbers = [3, 1, 7, 2, 5]
print(ind_maxlist(numbers))  # Выведет 2 (индекс числа 7)
