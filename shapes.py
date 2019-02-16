class Shape:
    def __init__(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def is_point_included(self, x, y):
        raise NotImplementedError()


class Point(Shape):
    def __init__(self, x, y):
        super().__init__(x, y)

    def is_point_included(self, x, y):
        return x == self.pos_x and y == self.pos_y


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        self.width = width
        self.height = height

    def is_point_included(self, x, y):
        return x >= self.pos_x and x < self.pos_x + self.width and \
            y >= self.pos_y and y < self.pos_y + self.height


class Square(Rectangle):
    def __init__(self, x, y, length):
        super().__init__(x, y, length, length)


class Circle(Shape):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius

    def is_point_included(self, x, y):
        count_circle = (x - self.pos_x) ** 2 + (y - self.pos_y) ** 2 - self.radius ** 2
        return count_circle <= 1