def sum_progress(a1, r, n):
    if n == 1:
        return a1
    
    current_term = a1 + (n - 1) * r
    return current_term + sum_progress(a1, r, n - 1)


# Пример: первый член 2, разность 3, найти сумму 4 членов (2+5+8+11 = 26)
print(sum_progress(2, 3, 4))
