class Shape:
    def __init__(self, x, y, color='X'):
        self.pos_x = x
        self.pos_y = y
        self.color = color

    def is_point_included(self, x, y):
        raise NotImplementedError()

    def move(self, on_x, on_y):
        self.pos_x += on_x
        self.pos_y += on_y


class Point(Shape):
    def __init__(self, x, y, color='X'):
        super().__init__(x, y, color)
        self.color = color

    def is_point_included(self, x, y):
        return x == self.pos_x and y == self.pos_y


class Rectangle(Shape):
    def __init__(self, x, y, width, height, color='X'):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def is_point_included(self, x, y):
        return x >= self.pos_x and x < self.pos_x + self.width and \
            y >= self.pos_y and y < self.pos_y + self.height


class Square(Rectangle):
    def __init__(self, x, y, length, color='X'):
        super().__init__(x, y, length, length, color)


class Circle(Shape):
    def __init__(self, x, y, radius, color='X'):
        super().__init__(x, y, color)
        self.radius = radius

    def is_point_included(self, x, y):
        count_circle = (x - self.pos_x) ** 2 + (y - self.pos_y) ** 2 - self.radius ** 2
        return count_circle <= 1