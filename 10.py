def maxlist(a):
    if len(a) == 1:
        return a[0]
    
    m = maxlist(a[1:])
    
    if a[0] > m:
        return a[0]
    
    return m


# Пример использования
numbers = [3, 1, 7, 2, 5]
print(maxlist(numbers))
