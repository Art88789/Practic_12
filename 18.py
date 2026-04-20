def simmetr(s, i, j):
    if i >= j:
        return True
    
    if s[i] != s[j]:
        return False

    return simmetr(s, i + 1, j - 1)


# Примеры использования
word = "шалаш"
print(simmetr(word, 0, 4))  # True

phrase = "река"
print(simmetr(phrase, 0, 3))  # False
