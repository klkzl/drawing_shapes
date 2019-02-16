class Shape:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y


class Point(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def is_included(self, x, y):
        return x == self.pos_x and y == self.pos_y