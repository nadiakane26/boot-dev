def args_logger(*args, **kwargs):
    for i, arg in enumerate(args):
        print(f"{i}. {arg}")
    for key, value in sorted(kwargs.items()):
        print(f"* {key}: {value}")