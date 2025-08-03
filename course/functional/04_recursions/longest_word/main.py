# def find_longest_word(document, longest_word=""):
    # words = document.split(" ")
    # for word in words:
    #     if len(word) > len(longest_word):
    #         longest_word = word
    # return longest_word

def find_longest_word(document, longest_word=""):
    if " " not in document:
        if len(document) > len(longest_word):
            return document
        else:
            return longest_word

    first_word, rest_of_string = document.split(" ", maxsplit=1)
    if len(first_word) > len(longest_word):
        longest_word = first_word
    return find_longest_word(rest_of_string, longest_word)
     
