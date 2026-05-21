def get_lcs_length(a, b, m, n):
    """Находит длину наибольшей общей подпоследовательности (НОП) двух строк.

    Вычисления производятся рекурсивным методом «сверху вниз» по длинам строк.
    """
    if m == 0 or n == 0:
        return 0

    if a[m - 1] == b[n - 1]:
        return 1 + get_lcs_length(a, b, m - 1, n - 1)

    res1 = get_lcs_length(a, b, m - 1, n)
    res2 = get_lcs_length(a, b, m, n - 1)

    return max(res1, res2)


# Пример использования
s1 = "ABCBDAB"
s2 = "BDCABA"
print(get_lcs_length(s1, s2, len(s1), len(s2)))  # Выведет 4
