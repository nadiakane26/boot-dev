def configure_plugin_decorator(func):
    # Create a wrapper function that takes positional arguments *args
    def wrapper(*args):
        # Convert the args into a dictionary
        kwargs = dict(args)
        # Return the result of passing this dictionary into func as keyword arguments unpacked with the ** operator
        return func(**kwargs)
    return wrapper

