"""
Name:Marietou Seck
greeting.py

Problem: This program will display a heart

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


from graphics import GraphWin, Circle, Polygon, Point, Text


def main():
    win_width = 500
    win_height = 500
    win = GraphWin("Heart", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    heart = Polygon(Point(-250,-250),Point(100,-350),Point(350,300), Point(300,-250))

    heart.setOutline("red")
    heart.setFill("red")
    heart.draw(win)


    win.getMouse()
    win.close()

main()
