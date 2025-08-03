def file_type_getter(file_extension_tuples):
    extension_to_type = {}
    for file_type, extensions in file_extension_tuples:
        # print (f"Processing file type: {file_type} with extensions: {extensions}")
        for ext in extensions:
            # print (f"Mapping extension: {ext} to file type: {file_type}")
            extension_to_type[ext] = file_type
            # print (f"Current mapping: {extension_to_type}")
    return lambda ext: extension_to_type.get(ext, "Unknown")