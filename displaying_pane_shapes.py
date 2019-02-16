from drawing_pane import ConsoleDrawingPane
from shapes import Circle, Point, Rectangle, Square

pane = ConsoleDrawingPane()

pane.shapes = [
    Point(10, 5, 'P'),
    Point(30, 3, 'P'),
    Rectangle(2, 1, 10, 3, 'R'),
    Square(38, 2, 7, 'S'),
    Circle(20, 5, 2, 'C')
]

pane.draw()