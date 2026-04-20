def ten_to_bin(x):
    if x < 2:
        return str(x)

    return ten_to_bin(x // 2) + str(x % 2)


# Пример использования
print(ten_to_bin(10))  # Выведет "1010"
print(ten_to_bin(25))  # Выведет "11001"
