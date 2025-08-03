def markdown_to_text_decorator(func):
    def wrapper(*args, **kwargs):
      # Map the *args to a new list where each string is converted to plain text using convert_md_to_txt
      new_args = list(map(convert_md_to_txt, args))
      # Map the **kwargs to a new dictionary where each "value" is converted to plain text using convert_md_to_txt. The "key" should remain the same.
      # Use the .items() dictionary method to pass a list of tuples of key-value pairs to map
      # Create a function for map which changes the value of an item tuple with convert_md_to_txt
      new_kwargs = dict(map(lambda item: (item[0], convert_md_to_txt(item[1])), kwargs.items()))
      return func(*new_args, **new_kwargs)
    return wrapper


# don't touch below this line


def convert_md_to_txt(doc):
    lines = doc.split("\n")
    for i in range(len(lines)):
        line = lines[i]
        lines[i] = line.lstrip("# ")
    return "\n".join(lines)
