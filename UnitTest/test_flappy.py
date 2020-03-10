"""""
Unit Testing of flappy.py
"""""

import os
import sys
import unittest

class flappyTestCase(unittest.TestCase):
    def test_flappy_inside(self):
        from freegames.flappy import inside
        from freegames.utils import vector

        testbounds = vector(150, 150)
        self.assertTrue(inside(testbounds))

        testpt = vector(90, 90)
        self.assertTrue(inside(testpt))

        testneg = vector(205, 205)
        self.assertFalse(inside(testneg))

