class ConsoleDrawingPane:
    def __init__(self, width=50, height=10):
        self.width = width
        self.height = height
        self.shapes = []

    def draw(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                symbol = '-'
                for shape in self.shapes:
                    if shape.is_point_included(x, y):
                        symbol = 'P'
                print(symbol, end='')
            print()