"""""
Unit testing of tictactoe.py
"""""

import os
import sys
import unittest
from freegames.tictactoe import floor

class tictactoeTestCase(unittest.TestCase):
    def test_tictactoe_floor(self):
        testvalue = 100
        val = floor(testvalue)
        print(val)

        testvalue2 = 200
        val2 = floor(testvalue2)
        print(testvalue2)


        self.assertEquals(val, 66)
        self.assertEquals(val2, 199)
