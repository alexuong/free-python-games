"""""
Unit testing of pong.py
"""""


import os
import sys
import unittest
from turtle import *
from freegames.pong import value
from freegames.utils import vector
class pongTestCase(unittest.TestCase):
    def test_value_pong(self):
        val = value();
        a = False
        if ((val >= -5 and val <= -3) or (val >= 3 and val <= 5)):
            a = True;
        else:
            a = False;
        self.assertEquals(a, True)
		
				
