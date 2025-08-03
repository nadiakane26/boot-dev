def new_resizer(max_width, max_height):
    def set_min_size(min_width = 0, min_height = 0):
        if min_width > max_width or min_height > max_height:
            raise ValueError("minimum size cannot exceed maximum size")
        def resize_image(width, height):
            width = max(min_width, min(width, max_width))
            height = max(min_height, min(height, max_height))
            return (width, height)
        return resize_image
    return set_min_size

print(new_resizer(800, 600)(200, 100)(1000, 500)) 