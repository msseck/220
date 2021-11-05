"""
Name:Marietou Seck
bumper.py

Problem: This program demonstrates the use of graphic packages and decision statements.

Certification of Authenticity:
I certify that this assignment is entirely my own work and discussed with: csl lab.
"""
from random import randint
from graphics import *


def main():
    width = 600
    height = 600
    win = GraphWin('Bumper', width, height)

    circle_ball = Circle(Point(width / 2, height / 2 - 30), 50)
    circle_ball.draw(win)
    circle_ball.setOutline("purple")
    circle_ball.setFill("purple")

    circle_ball2 = Circle(Point(width / 4, height / 4 - 30), 50)
    circle_ball2.draw(win)
    circle_ball2.setOutline("blue")
    circle_ball2.setFill("blue")
    dx = get_random(5)
    dy = get_random(5)

    if hit_vertical(circle_ball, win):
        dy = dy * -1
    if hit_horizontal(circle_ball, win):
        dx = dx * -1

    win.getMouse()
    win.close()


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def did_collide(circle_ball, circle_ball2):
    distance = ((circle_ball2.getX() - circle_ball.getX()) ** 2 + (circle_ball2.getY() - circle_ball.getY()) ** 2)
    circle_radius = circle_ball.getRadius()
    circle_radius2 = circle_ball2.getRadius()
    sum_radius = circle_radius2 + circle_radius
    if distance <= sum_radius:
        return True
    else:
        return False


def hit_vertical(circle_ball, win):
    circle_edge1 = circle_ball.getCenter().getY() + circle_ball.getRadius()
    circle_edge3 = circle_ball.getCenter().getY() + circle_ball.getRadius()
    circle_edge2 = circle_ball.getCenter().getY() - circle_ball.getRadius()
    circle_edge4 = circle_ball.getCenter().getY() - circle_ball.getRadius()
    if circle_edge1 or circle_edge3 >= win.getHeight() or circle_edge2 or circle_edge4 <= 0:
        return True
    else:
        return False


def hit_horizontal(circle_ball, win):
    circle_edge1 = circle_ball.getCenter().getX() + circle_ball.getRadius()
    circle_edge2 = circle_ball.getCenter().getX() - circle_ball.getRadius()
    if circle_edge1 >= win.getWidth() or circle_edge2 <= 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
