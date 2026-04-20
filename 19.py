def count(a, b):
    if a == b:
        return 1
    
    if a > b:
        return 1 + count(a - b, b)
    else:
        return 1 + count(a, b - a)


# Пример использования: прямоугольник 10 x 3
# Отрежутся квадраты: 3x3, 3x3, 3x3, 1x1, 1x1, 1x1. Всего 6.
print(count(10, 3))
