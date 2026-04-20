def progress(a1, r, n):
    if n == 1:
        return a1
    
    return progress(a1, r, n - 1) + r


# Пример: первый член 5, разность 2, найти 10-й член
print(progress(5, 2, 10))
