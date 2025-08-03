def count_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    unique = set(ch for ch in text if ch in vowels)
    count = sum(1 for ch in text if ch in vowels)
    return count, unique