def get_digit(digit):
    digits = "0123456789ABCDEF"
    return digits[digit]


def ten_to_n(x, n):
    if x < n:
        return get_digit(x)
    
    return ten_to_n(x // n, n) + get_digit(x % n)


# Примеры использования
print(ten_to_n(10, 2))   # Выведет "1010"
print(ten_to_n(255, 16)) # Выведет "FF"
print(ten_to_n(12, 8))   # Выведет "14"
