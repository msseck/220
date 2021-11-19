"""
Name:Marietou Seck
three_door_game.py

Problem: This program demonstrates ta user defined class.

Certification of Authenticity:
I certify that this assignment is entirely my own work and discussed with: csl lab.
"""

from graphics import*
from button import Button
from random import randint


def main():
    win = GraphWin("Three-Door-Game", 400, 400)
    shape1 = Rectangle(Point(130, 200), Point(170, 220))
    shape2 = Rectangle(Point(180, 200), Point(220, 220))
    shape3 = Rectangle(Point(230, 200), Point(270, 220))
    shape1.setOutline("black")
    shape2.setOutline("black")
    shape3.setOutline("black")
    button1 = Button(shape1, "Door1")
    button2 = Button(shape2, "Door2")
    button3 = Button(shape3, "Door3")
    button1.draw(win)
    button2.draw(win)
    button3.draw(win)
    buttons = [button1, button2, button3]
    correct_button = buttons[randint(0, 2)]

    msg = Text(Point(200, 50), "I have a secret door")
    msg.draw(win)

    msg2 = Text(Point(200, 350), "Click to choose my door")
    msg2.draw(win)
    click = win.getMouse()

    for i in buttons:
        if i.is_clicked(click):
            if i == correct_button:
                msg.setText("You Win!")
                i.color_button("green")
                msg2.setText("Click to close")
            else:
                msg.setText("You Lost!")
                i.color_button("red")
                msg2.setText(i.get_label() + " is my secret door")

    win.getMouse()
    win.close()


if __name__ == '__main__':
    main()
