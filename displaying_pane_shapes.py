from drawing_pane import ConsoleDrawingPane
from shapes import Circle, Point, Rectangle, Square

pane = ConsoleDrawingPane()

pane.shapes = [
    Point(10, 5),
    Point(30, 3),
    Rectangle(2, 1, 10, 3),
    Square(40, 3, 5),
    Circle(20, 5, 2)
]

pane.draw()