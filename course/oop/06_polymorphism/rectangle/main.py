class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x1, y1, x2, y2):
        return (
            self.pos_x >= x1
            and self.pos_x <= x2
            and self.pos_y >= y1
            and self.pos_y <= y2
        )

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, height, width, fire_range):
        # Call constructor of the Unit class with the provided parameters
        super().__init__(name, pos_x, pos_y)
        # Set the dragon-specific parameters as instance variables
        self.height = height
        self.width = width
        self.fire_range = fire_range

        x1 = pos_x - width / 2
        y1 = pos_y - height / 2
        x2 = pos_x + width / 2
        y2 = pos_y + height / 2

        # Create a hit box for the dragon using the Rectangle class
        self.__hit_box = Rectangle(x1, y1, x2, y2)

    def in_area(self, x1, y1, x2, y2):
        # Create a new rectangle object with the given corner positions.
        area = Rectangle(x1, y1, x2, y2)

        # Check if this rectangle overlaps with the dragon's hit box
        return self.__hit_box.overlaps(area)

class Rectangle:
    def overlaps(self, rect):
        return (
            # self's left side is on or to the left of B's right side
            self.get_left_x() <= rect.get_right_x() and
            # self's right side is on or to the right of B's left side
            self.get_right_x() >= rect.get_left_x() and
            # self's top side is on or above B's bottom side
            self.get_top_y() >= rect.get_bottom_y() and
            # self's bottom side is on or below B's top side
            self.get_bottom_y() <= rect.get_top_y()
        )

    def __init__(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
    
    def get_left_x(self):
        # return min(self.x1, self.x2)
        if self.__x1 < self.__x2:
            return self.__x1
        return self.__x2

    def get_right_x(self):
        # return max(self.x1, self.x2)
        if self.__x1 > self.__x2:
            return self.__x1
        return self.__x2

    def get_top_y(self):
        # return max(self.y1, self.y2)
        if self.__y1 > self.__y2:
            return self.__y1
        return self.__y2

    def get_bottom_y(self):
        # return min(self.y1, self.y2)
        if self.__y1 < self.__y2:
            return self.__y1
        return self.__y2

    def __repr__(self):
        return f"Rectangle({self.__x1}, {self.__y1}, {self.__x2}, {self.__y2})"
