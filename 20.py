def comp(a, b, m, n):
    if m == 0 or n == 0:
        return 0

    if a[m - 1] == b[n - 1]:
        return 1 + comp(a, b, m - 1, n - 1)

    res1 = comp(a, b, m - 1, n)
    res2 = comp(a, b, m, n - 1)
    
    if res1 > res2:
        return res1
    else:
        return res2


# Пример использования
s1 = "ABCBDAB"
s2 = "BDCABA"
print(comp(s1, s2, len(s1), len(s2)))  # Выведет 4
