def count(n):
    if n < 10:
        return 1
    
    return 1 + count(n // 10)


# Пример использования
result = count(12345)
print(result)
