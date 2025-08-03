def count_nested_levels(nested_documents, target_document_id, level=1):
    for doc_id, children in nested_documents.items():
        # If the current document_id matches the target_document_id, return its level of nesting
        if doc_id == target_document_id:
            return level
        # If the target_document_id is not found, recursively call count_nested_levels on the current document_id and increment the level
        if children:
            nested_result = count_nested_levels(children, target_document_id, level + 1) 
            if nested_result != -1:
                return nested_result
    return -1