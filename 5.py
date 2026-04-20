def mod_number(a, b):
    if a < b:
        return a
    
    return mod_number(a - b, b)


# Пример использования: 17 разделить на 5, остаток 2
print(mod_number(17, 5))
