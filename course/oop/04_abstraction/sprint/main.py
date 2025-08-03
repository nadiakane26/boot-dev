class Human:
    def sprint_right(self):
        self.__sprint(self.move_right)

    def sprint_left(self):
        self.__sprint(self.move_left)

    def sprint_up(self):
        self.__sprint(self.move_up)

    def sprint_down(self):
        self.__sprint(self.move_down)

    def __sprint(self, direction_function):
        self.__raise_if_cannot_sprint()
        self.__use_sprint_stamina()
        direction_function()
        direction_function()

    def __raise_if_cannot_sprint(self):
        if self.__stamina <= 0:
            raise Exception("not enough stamina to sprint")

    def __use_sprint_stamina(self):
        self.__stamina -= 1

    # don't touch below this line

    def move_right(self):
        self.__pos_x += self.__speed

    def move_left(self):
        self.__pos_x -= self.__speed

    def move_up(self):
        self.__pos_y += self.__speed

    def move_down(self):
        self.__pos_y -= self.__speed

    def get_position(self):
        return self.__pos_x, self.__pos_y

    def __init__(self, pos_x, pos_y, speed, stamina):
        self.__pos_x = pos_x
        self.__pos_y = pos_y
        self.__speed = speed
        self.__stamina = stamina
