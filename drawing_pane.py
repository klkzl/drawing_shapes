class ConsoleDrawingPane:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        for y in range(0, self.height):
            for x in range(0, self.width):
                print('X', end='')
            print()