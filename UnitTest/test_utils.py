"""
Unit testing of utils.py
"""

import os
import sys
import unittest
from UnitTest.testLib import md5
from freegames.utils import floor


class utilsTestCase(unittest.TestCase):
    
    def test_utils_md5sum(self):
        # test that the file has not changed
        md5_exp = '6dd9c90b964585f94726c38775a779b2'
        cwd = os.getcwd()
        path = cwd + '/freegames/utils.py'
        if os.path.isfile(path):
            md5_act = md5(path)
        self.assertEqual(md5_exp, md5_act)
    
    def test_floor(self):
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