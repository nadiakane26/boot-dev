def replacer(old, new):
    def replace(decorated_func):
        # replace takes an input function, decorated_func, and returns a wrapper function.
        def wrapper(text):
            # wrapper takes as input a string text. It uses .replace() string method to replace instances of old with new in the text.
            modified_text = text.replace(old, new)
            # Returns the result of passing the modified text to the decorated_func.
            return decorated_func(modified_text)
        return wrapper
    return replace

# Use a series of the replacer function to decorate tag_pre
@replacer("&", "&amp;")
@replacer("<", "&lt;")
@replacer(">", "&gt;")
@replacer('"', "&quot;")
@replacer("'", "&#x27;")
def tag_pre(text):
    return f"<pre>{text}</pre>"

