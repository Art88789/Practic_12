def combin(n, k):
    if k == 0 or k == n:
        return 1
    
    if k > n:
        return 0
    
    return combin(n - 1, k - 1) + combin(n - 1, k)


# Пример использования: сочетание из 5 по 3 (равно 10)
print(combin(5, 3))
