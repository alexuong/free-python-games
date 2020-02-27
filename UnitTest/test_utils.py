"""
Unit testing of utils.py
"""

import os
import sys
import unittest
from UnitTest.testLib import md5, winOrLin
from freegames.utils import floor, path

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