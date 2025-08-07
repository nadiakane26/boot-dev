from stack import Stack


def is_balanced(input_str):
    """
    Checks if the parentheses in the input string are balanced.

    Args:
        input_str (str): The string to check for balanced parentheses.

    Returns:
        bool: True if the parentheses are balanced, False otherwise.
    """
    stack = Stack() # Create a new stack instance
    opening = "("
    closing = ")"
    
    for char in input_str: # Iterate through each character in the input string
        if char in opening: # Check if the character is an opening parenthesis
            stack.push(char) # append to the stack
        elif char in closing: # Check if the character is a closing parenthesis
            if stack.size() == 0: # If the stack is empty, it means there's no matching opening parenthesis
                return False
            stack.pop() # Pop the top item from the stack
    
    return stack.size() == 0 # If the stack is empty after processing all characters, the parentheses are balanced

