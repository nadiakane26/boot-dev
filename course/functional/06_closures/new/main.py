import copy

def css_styles(initial_styles):
    # Copies nested dictionary
    styles = copy.deepcopy(initial_styles)
    def add_style(selector, property, value):
        # Checks if the selector exists in the dictionary. If not, creates a new dictionary for the selector value.
        styles[selector] = styles.get(selector, {})
        # Adds or updates the property with the given value for the selector.
        styles[selector][property] = value
        return styles
    return add_style