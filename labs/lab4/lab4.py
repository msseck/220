"""
Name:Marietou Seck
lab4.py

Problem: practice accumulating sequence using python graphics .

Certification of Authenticity:
I certify that this assignment is entirely my own work.

"""

from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can draw additional circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to draw an additional square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(200, 200), Point(150, 150))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        # centerPoint = shape.getCenter()
        # center of square

        dx = p.getX()
        dy = p.getY()
        # shape.move(dx, dy)

        shape = Rectangle(Point(dx - 25, dy - 25), Point(dx + 25, dy + 25))
        shape.setOutline("blue")
        shape.setFill("blue")
        shape.draw(win)

        # move amount is distance from center of circle to the
        # point where the user clicked
        # dx = p.getX() - centerPoint.getX()
        # dy = p.getY() - centerPoint.getY()

    instructions.undraw()
    final_sq = Point(width / 2, height - 10)
    message = Text(final_sq, "Click again to quit")
    message.draw(win)

    # win.getMouse()
    # win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()

    shape = Rectangle(p1, p2)
    shape.setOutline("purple")
    shape.setFill("purple")
    shape.draw(win)

    length_x = abs(p1.getX() - p2.getX())
    length_y = abs(p1.getY() - p2.getY())
    perimeter = 2 * length_y + 2 * length_x
    area = length_x * length_y

    perimeter_message = Point(width / 25, height - 60)
    print_message = Text(perimeter_message, perimeter)
    print_message.draw(win)

    area_message = Point(width / 20, height - 20)
    end_message = Text(area_message, area)
    end_message.draw(win)

    placement = Point(width / 2, height - 10)
    message = Text(placement, "Click to end the program")
    message.draw(win)

    win.getMouse()
    win.close()


def circle():
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    p1 = win.getMouse()
    p2 = win.getMouse()

    radius = ((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)**(1/2)

    shape = Circle(p1, radius)
    shape.setOutline("purple")
    shape.setFill("purple")
    shape.draw(win)

    radius_message = Point(width / 5, height - 10)
    end_message = Text(radius_message, radius)
    end_message.draw(win)

    last_message = Point(width / 2, height - 10)
    message = Text(last_message, "Click to end the program")
    message.draw(win)

    win.getMouse()
    win.close()


def pi2():
    num_of_terms = eval(input("What is the number of terms to sum?:"))
    numer = 4
    for i in range(num_of_terms):
        denom = denom + 2


def main():
    squares()
    rectangle()
    circle()
    pi2()


main()
