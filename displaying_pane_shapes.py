from drawing_pane import ConsoleDrawingPane
from shapes import Point, Rectangle

pane = ConsoleDrawingPane()

pane.shapes = [
    Point(10, 5),
    Point(30, 3),
    Rectangle(2, 1, 10, 3)
]

pane.draw()