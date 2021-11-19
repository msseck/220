"""
Name:Marietou Seck
button.py

Problem: This program demonstrates ta user defined class.

Certification of Authenticity:
I certify that this assignment is entirely my own work and discussed with: csl lab.
"""
from graphics import*


class Button:
    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)

    def get_label(self):
        return self.text.getText()

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        p1x = self.shape.getP1().getX()
        p1y = self.shape.getP1().getY()
        p2x = self.shape.getP2().getX()
        p2y = self.shape.getP2().getY()
        pointx = point.getX()
        pointy = point.getY()

        if p1x <= pointx <= p2x and p1y <= pointy <= p2y:
            return True
        else:
            return False

    def color_button(self, color):
        self.shape.setFill(color)

    def set_label(self, label):
        self.text.setText(label)
