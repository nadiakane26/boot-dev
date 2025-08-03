import functools



sentences, n = ["This is the first sentence", "This is the second sentence", "This is the third sentence", "This is the fourth sentence"], 3

def join(doc_so_far, sentence):
    return doc_so_far + ". " + sentence if doc_so_far else sentence


def join_first_sentences(sentences, n):
    if n <= 0:
        return ""
    else:
        return functools.reduce(join, sentences[:n], "").strip() + "." if sentences else ""

join_first_sentences(sentences, n)