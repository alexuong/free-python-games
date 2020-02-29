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
        
    def test_utils_eq(self):
        act = vector(1, 2)
        w = vector(1, 2)
        z = vector(1, 3)
        x = vector(3, 2)
        self.assertEquals(True, act == w)
        self.assertEquals(False, act == z)
        self.assertEquals(False, act == x)
        self.assertEquals(False, act == 4)

    def test_utils_ne(self):
        act = vector(1, 2)
        w = vector(1, 2)
        z = vector(1, 3)
        x = vector(3, 2)
        self.assertEquals(False, act != w)
        self.assertEquals(True, act != z)
        self.assertEquals(True, act != x)
        self.assertEquals(True, act != 4)

    def test_utils_iadd(self):
        exp_x = 4
        exp_y = 6
        act = vector(1, 2)
        w = vector(3, 4)
        act += w
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        h = hash(act)
        with self.assertRaises(Exception): act += w

    def test_utils_add(self):
        exp_x = 4
        exp_y = 6
        v = vector(1, 2)
        w = vector(3, 4)
        act = v + w
        self.assertEquals(False, act is v)
        self.assertEquals(False, act is w)
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)

    def test_utils_isub(self):
        exp_x = -2
        exp_y = -2
        act = vector(1, 2)
        w = vector(3, 4)
        act -= w
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        h = hash(act)
        with self.assertRaises(Exception): act -= w

    def test_utils_sub(self):
        exp_x = -2
        exp_y = -2
        v = vector(1, 2)
        w = vector(3, 4)
        act = v - w
        self.assertEquals(False, act is v)
        self.assertEquals(False, act is w)
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)

    def test_utils_imul(self):
        exp_x = 3
        exp_y = 8
        act = vector(1, 2)
        w = vector(3, 4)
        act *= w
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check multiplying by normal numbers
        exp_x = 3
        exp_y = 6
        act = vector(1, 2)
        act *= 3
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check hash
        h = hash(act)
        with self.assertRaises(Exception): act *= w

    def test_utils_mul(self):
        exp_x = 3
        exp_y = 8
        v = vector(1, 2)
        w = vector(3, 4)
        act = v * w
        self.assertEquals(False, act is v)
        self.assertEquals(False, act is w)
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check multiplying by normal numbers
        exp_x = 3
        exp_y = 6
        v = vector(1, 2)
        act = v * 3
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check right hand multiplying by normal numbers
        exp_x = 3
        exp_y = 6
        v = vector(1, 2)
        act = 3 * v
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)

    def test_utils_scale(self):
        # Check scaling with vector
        exp_x = 3
        exp_y = 8
        act = vector(1, 2)
        w = vector(3, 4)
        act.scale(w)
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check scaling with normal numbers
        exp_x = 3
        exp_y = 6
        act = vector(1, 2)
        act.scale(3)
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)

    def test_utils_itruediv(self):
        exp_x = 3
        exp_y = 2
        act = vector(3, 4)
        w = vector(1, 2)
        act /= w
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check dividing by normal numbers
        exp_x = 1
        exp_y = 2
        act = vector(2, 4)
        act /= 2
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check hash
        h = hash(act)
        with self.assertRaises(Exception): act /= w

    def test_utils_truediv(self):
        exp_x = 3
        exp_y = 2
        v = vector(3, 4)
        w = vector(1, 2)
        act = v / w
        self.assertEquals(False, act is v)
        self.assertEquals(False, act is w)
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check dividing by normal numbers
        exp_x = 1
        exp_y = 2
        v = vector(2, 4)
        act = v /2
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)

    def test_utils_neg(self):
        exp_x = -1
        exp_y = -2
        v = vector(1, 2)
        act = -v
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        self.assertEquals(False, v is -v)

    def test_utils_abs(self):
        exp = 5
        v = vector(3, 4)
        act = abs(v)
        self.assertEquals(exp, act)

    def test_utils_rotate(self):
        # Check positive rotation
        exp_x = -2
        exp_y = 1
        act = vector(1, 2)
        act.rotate(90)
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)
        # Check negative rotation
        exp_x = 1
        exp_y = 2
        act.rotate(-90)
        self.assertEquals(exp_x, act.x)
        self.assertEquals(exp_y, act.y)

    def test_utils_repr(self):
        exp = 'vector(1, 2)'
        v = vector(1, 2)
        act = repr(v)
        self.assertEquals(exp, act)
