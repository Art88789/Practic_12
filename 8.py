def fib(k):
    if k == 1 or k == 2:
        return 1
    
    return fib(k - 1) + fib(k - 2)


# Пример: 7-й член последовательности Фибоначчи (1, 1, 2, 3, 5, 8, 13)
print(fib(7))
