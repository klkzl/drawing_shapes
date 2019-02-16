from drawing_pane import ConsoleDrawingPane
from shapes import Point

pane = ConsoleDrawingPane()

pane.shapes = [
    Point(10, 5)
]

pane.draw()