valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    # if not doc_names or not doc_formats:
    #     return []

    pairs = zip(doc_names, doc_formats)
    return list(filter(lambda tup: tup[1] in valid_formats, pairs))
