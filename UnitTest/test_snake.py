"""""
Unit Testing of snake.py
"""""

import os
import sys
import unittest

class snakeTestCase(unittest.TestCase):
    def test_snake_change(self):
        from freegames.snake import change, aim
        from freegames.utils import vector
  
        aim = vector(0, -10)
        changevector = vector(10, 15)
        change(changevector.x, changevector.y)
        self.assertEquals(10, aim.x)
        self.assertEquals(15, aim.y)

    def test_snake_inside(self):
        from freegames.flappy import inside
        from freegames.utils import vector

        testbounds = vector(150, 150)
        self.assertTrue(inside(testbounds))

        testpt = vector(90, 90)
        self.assertTrue(inside(testpt))

        testneg = vector(205, 205)
        self.assertFalse(inside(testneg))



