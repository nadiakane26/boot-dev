def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char.isalpha():
            char_dict[char] = char_dict.get(char, 0) + 1
    return char_dict
        
def sort_char_count(char_dict):
    sorted_chars = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)
    return sorted_chars       
    