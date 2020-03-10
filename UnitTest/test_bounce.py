"""
unit testing of bounce.py
"""


import os
import sys
import unittest
from turtle import *
from freegames.utils import vector


class bounceTestCase(unittest.TestCase):
    def test_bounce_draw(self):
        from freegames.bounce import ball, aim, draw
        aim = vector(201, -201)
        ball = vector(201, -201)
	ball.x = 201
	ball.y = -201
	draw()
	self.assertEquals(201, aim.x)
        self.assertEquals(-201, aim.y)



    def test_bounce_value(self):
        from freegames.bounce import value
        val = value();
        a = False
        if ((val >= -5 and val <= -3) or (val >= 3 and val <= 5)):
            a = True;
        else:
            a = False;
        self.assertEquals(a, True)
 
