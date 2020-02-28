"""
Unit testing of utils.py
"""

import os
import sys
import unittest
from UnitTest.testLib import md5, winOrLin
from freegames.utils import floor, path, vector

slash, isWin = winOrLin()


class utilsTestCase(unittest.TestCase):
    
    def test_utils_md5sum(self):
        # test that the file has not changed
        md5_exp = '6dd9c90b964585f94726c38775a779b2'
        cwd = os.getcwd()
        path = cwd + '/freegames/utils.py'
        if os.path.isfile(path):
            md5_act = md5(path)
        self.assertEqual(md5_exp, md5_act)
    
    def test_utils_floor(self):
        # Positive Test
        exp = 0.0
        act = floor(10.0, 100.0)
        self.assertEqual(exp, act)
        # Boundary Test1
        exp = -200.0
        act = floor(-200.0, 100.0)
        self.assertEqual(exp, act)
        # Boundary Test2
        exp = 200.0
        act = floor(200.0, 100.0)
        self.assertEqual(exp, act)
    
    def test_utils_path(self):
        # Positive Test
        cwd = os.getcwd()
        testFile = 'pacman.py'
        expPath = cwd + slash+ 'freegames' + slash + testFile
        actPath = path(testFile)
        self.assertEqual(expPath, actPath)
    
    def test_utils_line(self):
        # TODO: add tests that use Turtle
        pass
    
    def test_utils_square(self):
        # TODO: add tests that use Turtle
        pass


# Vector Class
    def test_utils_init(self):
        exp_x = 1
        exp_y = 2
        act = vector(1, 2)
        self.assertEqual(exp_x, act.x)
        self.assertEqual(exp_y, act.y)

    def test_utils_x(self):
        exp_x = 3
        exp_y = 2
        act = vector(1, 2)
        act.x = 3
        self.assertEqual(exp_x, act.x)
        self.assertEqual(exp_y, act.y)

    def test_utils_y(self):
        exp_x = 1
        exp_y = 4
        act = vector(1, 2)
        act.y = 4
        self.assertEqual(exp_x, act.x)
        self.assertEqual(exp_y, act.y)

    def test_utils_hash(self):
        act = vector(1, 2)
        h = hash(act)
        with self.assertRaises(Exception): act.x = 3

    def test_utils_len(self):
        exp = 2
        v = vector(1, 5)
        act = len(v)
        self.assertEqual(exp, act)

    def test_utils_getitem(self):
        exp_x = 3
        exp_y = 4
        act = vector(3, 4)
        self.assertEqual(exp_x, act[0])
        self.assertEqual(exp_y, act[1])
        with self.assertRaises(Exception): act[2]

    def test_utils_copy(self):
        exp_x = 1
        exp_y = 2
        v = vector(1, 2)
        c = v.copy()
        self.assertEquals(False, v is c)
        self.assertEquals(exp_x, c.x)
        self.assertEquals(exp_y, c.y)
        
