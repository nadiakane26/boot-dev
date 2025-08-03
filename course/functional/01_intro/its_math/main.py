def get_median_font_size(font_sizes):
    """
    Calculate the median font size from a list of font sizes.

    :param font_sizes: List of font sizes (integers).
    :return: The median font size or None if the list is empty.
    """
    if not font_sizes:
        return None
    
    sorted_sizes = sorted(font_sizes)
    n = len(sorted_sizes)
    
    if n % 2 == 1:
        # If odd, return the middle element
        return sorted_sizes[n // 2]
    else:
        # If even, return the lowest of the two middle elements
        mid1 = sorted_sizes[n // 2 - 1]
        mid2 = sorted_sizes[n // 2]
        return min(mid1, mid2) 