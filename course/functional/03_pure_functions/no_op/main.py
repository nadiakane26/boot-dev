def remove_emphasis_from_word(word):
    return word.strip("*")

def remove_emphasis_from_line(line):
    words = line.split(" ")
    cleaned_words = list(map(remove_emphasis_from_word, words))
    return " ".join(cleaned_words)

    
def remove_emphasis(doc_content):
    lines = doc_content.split("\n")
    cleaned_lines = list(map(remove_emphasis_from_line, lines))
    return "\n".join(cleaned_lines)
