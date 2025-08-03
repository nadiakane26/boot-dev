
def area_sum(rectangles):
    total_sum = 0
    for rect in rectangles:
        if "height" in rect and "width" in rect:
            area = rect["height"] * rect["width"]
            total_sum += area
    return total_sum

