def new_collection(initial_docs):
    """initial_docs: a list of strings."""
    docs = initial_docs.copy()
    def add(doc):
        docs.append(doc)
        return docs
    return add
