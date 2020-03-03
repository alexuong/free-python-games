"""
Unit testing of cannon.py
"""

import os
import sys
import unittest
from turtle import *
from unittest.mock import MagicMock, patch
from UnitTest.testLib import md5
from freegames.utils import vector


class cannonTestCase(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('turtle.Turtle')
        self.MockTurtle = self.patcher.start()
    
    def tearDown(self):
        self.patcher.stop()
    
    def test_cannon_md5sum(self):
        # test that the file has not changed
        md5_exp = 'd17b1cedfb5e068fda6dd8d043620e93'
        cwd = os.getcwd()
        path = cwd + '/freegames/cannon.py'
        if os.path.isfile(path):
            md5_act = md5(path)
        self.assertEqual(md5_exp, md5_act)
    
    def test_cannon_tap(self):
        from freegames.cannon import tap, ball, speed
        # Positive Test
        ball.x = 201
        ball.y = -201
        point = vector(100, 100)
        tap(point.x, point.y)
        self.assertEqual(ball.x, -199)
        self.assertEqual(ball.y, -199)
        self.assertEqual(speed.x, 12)
        self.assertEqual(speed.y, 12)
        # Negative Test
        ball.x = 199
        ball.y = -199
        speed.x = 0
        speed.y = 0
        point = vector(100, 100)
        tap(point.x, point.y)
        self.assertEqual(ball.x, 199)
        self.assertEqual(ball.y, -199)
        self.assertEqual(speed.x, 0)
        self.assertEqual(speed.y, 0)
    
    def test_cannon_inside(self):
        from freegames.cannon import inside
        # Positive Test
        point = vector(100, 100)
        self.assertTrue(inside(point))
        # Negative Test
        point = vector(201, 201)
        self.assertFalse(inside(point))
        # Boundary Test
        point = vector(199, 199)
        self.assertTrue(inside(point))
        # Boundary Test
        point = vector(-199, -199)
        self.assertTrue(inside(point))
    
    def test_cannon_draw(self):
        #TODO: test the draw function
        pass
    
    def test_cannon_move(self):
        #TODO: test the move function
        pass

