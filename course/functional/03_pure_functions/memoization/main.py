def word_count_memo(document, memos):
    new_memos = memos.copy()
    if document in new_memos:
        return new_memos[document], new_memos
    else:
        count = word_count(document)
        new_memos[document] = count
        return count, new_memos


# Don't edit below this line


def word_count(document):
    count = len(document.split())
    return count

