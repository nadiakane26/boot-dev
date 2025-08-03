def doc_format_checker_and_converter(conversion_function, valid_formats):
    def check_and_convert(filename, content):
        if not filename.endswith(tuple(valid_formats)):
            raise ValueError(f"invalid file format")
        return conversion_function(content)
    return check_and_convert

# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]

