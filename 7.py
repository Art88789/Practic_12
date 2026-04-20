def nod(a, b):
    if b == 0:
        return a
    
    return nod(b, a % b)


# Пример использования: НОД для 48 и 18 равен 6
print(nod(48, 18))
