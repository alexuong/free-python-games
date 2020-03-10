"""
unit testing of bounce.py
"""


import os
import sys
import unittest
from turtle import *
from freegames.utils import vector


class memoryTestCase(unittest.TestCase):
    def test_memory_index(self):
        from freegames.memory import index
        testx = 100
        testy = 200
        
        output = index(testx, testy)

        self.assertEquals(output, 70)

    def test_memory_xy(self):
        from freegames.memory import xy
        num = 50
        compare = xy(num)
        self.assertEquals((-100, 100), compare)



