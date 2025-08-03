def word_count_aggregator():
    """
    Returns a function that counts the number of words in a document.
    The returned function can be called with a document string to get the word count.
    """
    count = 0
    def count_words(document):
        nonlocal count
        count += len(document.split())
        return count

    return count_words