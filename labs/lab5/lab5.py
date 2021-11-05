"""
Name:Marietou Seck
lab5.py

Problem: This program is meant to display python graphics

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import *
import math


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Add code here to accept the mouse clicks, draw the triangle.
    # and display its area in the graphics window.

    p1 = win.getMouse()
    p2 = win.getMouse()
    p3 = win.getMouse()

    shape = Polygon(p1, p2, p3)
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    line1 = p1.getX()-p1.getY()
    line2 = p2.getX()-p2.getY()
    line3 = p3.getX()-p3.getY()
    length1 = math.sqrt(line1**2 + line2**2)
    length2 = math.sqrt(line2**2 + line3**2)
    length3 = math.sqrt(line3**2 + line1**2)
    length = length1 + length2 + length3
    s = (length1 + length2 + length3)/2
    area = math.sqrt(s*(s-length1)*(s-length2)*(s-length3))

    first_message = Point(win_width / 2, win_height - 10)
    message = Text(first_message, "The perimeter is: " + str(length))
    last_message = Point(win_width / 4, win_height - 20)
    message_area = Text(last_message,  "The area is: " + str(area))
    message.draw(win)
    message_area.draw(win)
    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_input = Entry(Point(win_width / 2 - 18, win_height / 2 + 40), 5)
    red_input.draw(win)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_input = Entry(Point(win_width / 2 - 11, win_height / 2 + 70), 5)
    green_input.draw(win)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_input = Entry(Point(win_width / 2 - 15, win_height / 2 + 100), 5)
    blue_input.draw(win)

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)

    for i in range(5):
        win.getMouse()
        green = green_input.getText()
        blue = blue_input.getText()
        red = red_input.getText()

        color_mixer = color_rgb(eval(red), eval(green), eval(blue))

        shape.setFill(color_mixer)

    # Wait for another click to exit
    inst.undraw()
    inst.setText("Click to close the window. ")
    inst.draw(win)
    win.getMouse()
    win.close()


def process_string():
    user_input = (input("Enter a sentence:"))
    first_charc = user_input[0]
    print(first_charc)
    last_ch = user_input[-1]
    print(last_ch)
    incl = user_input[2:6]
    print(incl)
    first_last = first_charc + last_ch
    print(first_last)
    first_three = user_input[0:3] * 10
    print(first_three)
    for i in range(len(user_input)):
        special = user_input[i]
        print(special)
    print("The number of characters are:", len(user_input))


def main():
    #triangle()
    color_shape()
    #process_string()

    pass


main()
