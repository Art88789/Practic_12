def is_palindrome(s, i, j):
    """Рекурсивно проверяет, является ли подстрока от индекса i до j палиндромом.
    """
    if i >= j:
        return True

    if s[i] != s[j]:
        return False

    return is_palindrome(s, i + 1, j - 1)


# Примеры использования
word = "шалаш"
print(is_palindrome(word, 0, 4))  # True

phrase = "река"
print(is_palindrome(phrase, 0, 3))  # False
