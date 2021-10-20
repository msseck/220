"""
Name:Marietou Seck
vigenere.py

Problem: This program will implement the vignere cipher.

Certification of Authenticity:
I certify that this assignment is entirely my own work,
 but I discussed it with: Angela Nganga.
"""
from graphics import *


def code(message, keyword):
    none = ''
    msgr = message.getText()
    keyw = keyword.getText()
    for i in range(len(msgr)):
        encode = chr((ord(msgr[0])) + ord(keyw[0]) % 26)
        none += encode
    return none


def main():
    win = GraphWin("Vingenere", 500, 300)
    win.setCoords(0, 0, 10, 10)
    # message to code
    msg_code = Text(Point(2, 9), "Message to code")
    msg_code.draw(win)
    # message to code input
    message = Entry(Point(6.5, 9), 41)
    message.draw(win)
    # enter keyword prompt
    key = Text(Point(2, 7), "Enter Keyword")
    key.draw(win)
    # keyword input
    keyword = Entry(Point(5, 7), 17)
    keyword.draw(win)
    # encode button
    button_text = Text(Point(5, 5.5), "Encode")
    button_outline = Rectangle(Point(4, 6), Point(6, 5))
    button_text.draw(win)
    button_outline.draw(win)

    win.getMouse()


if __name__ == "__main__":
    main()
