def file_to_prompt(file, to_string):
    """
    Converts a file dictionary to a formatted string prompt.

    Args:
        file (dict): A dictionary containing file details.
        to_string (function): A function to convert the content to a string.

    Returns:
        str: A formatted string representation of the file.
    """
    return f"```\n{to_string(file)}\n```"