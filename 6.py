def degree5(n):
    if n == 1:
        return 0
    
    if n < 5 or n % 5 != 0:
        return -1
    
    res = degree5(n // 5)
    
    if res == -1:
        return -1
    
    return 1 + res


# Примеры использования
print(degree5(125))  # Выведет 3 (5^3 = 125)
print(degree5(20))   # Выведет -1 (не степень 5)
print(degree5(1))    # Выведет 0 (5^0 = 1)
