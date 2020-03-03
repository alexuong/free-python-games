"""
Unit testing of pacman.py
"""

import os
import sys
import unittest
from turtle import *
from unittest.mock import MagicMock, patch
from UnitTest.testLib import md5
from freegames.utils import vector


class pacmanTestCase(unittest.TestCase):
    def setUp(self):
        self.patcher = patch('turtle.Turtle')
        self.MockTurtle = self.patcher.start()
    
    def tearDown(self):
        self.patcher.stop()
    
    def test_pacman_md5sum(self):
        # test that the file has not changed
        md5_exp = 'bf6dc6a7523699c5376eb3d02222d1b3'
        cwd = os.getcwd()
        path = cwd + '/freegames/pacman.py'
        if os.path.isfile(path):
            md5_act = md5(path)
        self.assertEqual(md5_exp, md5_act)
    
    def test_pacman_square(self):
        from freegames.pacman import square
        #TODO: test this function
        pass
    
    def test_pacman_offset(self):
        from freegames.pacman import offset
        # test 1
        point = vector(100,100)
        act = offset(point)
        exp = 95
        self.assertEqual(act, exp)
        # test 2
        point = vector(0,0)
        act = offset(point)
        exp =190
        self.assertEqual(act, exp)
        # test 3
        point = vector(200,200)
        act = offset(point)
        exp = 0
        self.assertEqual(act, exp)
        # test 4
        point = vector(-220,-220)
        act = offset(point)
        exp = 399
        self.assertEqual(act, exp)
    
    def test_pacman_valid(self):
        from freegames.pacman import valid
        # Positive Test
        point = vector(100,100)
        self.assertTrue(valid(point))
        # Negative Test
        point = vector(101,101)
        self.assertFalse(valid(point))
        # Boundary Test 1
        point = vector(200,200)
        self.assertFalse(valid(point))
        # Boundary Test 2
        point = vector(-220,-220)
        self.assertFalse(valid(point))
    
    def test_pacman_world(self):
        from freegames.pacman import world
        #TODO: test this function
        pass
    
    def test_pacman_move(self):
        from freegames.pacman import move
        #TODO: test this function
        pass
    
    def test_pacman_change(self):
        from freegames.pacman import change, aim
        # Positive Test
        newDir = vector(100, 100)
        change(newDir.x, newDir.y)
        self.assertEqual(newDir.x, aim.x)
        self.assertEqual(newDir.y, aim.y)
        # Negative Test
        newDir = vector(200, 200)
        change(newDir.x, newDir.y)
        self.assertEqual(100, aim.x)
        self.assertEqual(100, aim.y)