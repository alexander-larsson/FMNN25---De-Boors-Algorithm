# -*- coding: utf-8 -*-
import numpy as np
import scipy as sp
import unittest as ut
from Spline import *
"""
Created on Tue Sep  1 14:16:15 2015
@author: Olle Tervalampi-Olsson
"""


class TestSplineCreation(ut.TestCase):
    def helpTest(self, points, deg):
        s = Spline(points,deg)
        self.assertAlmostEqual(s.p, deg)
        np.testing.assert_array_equal(s.d, points)
    def testPositivePointsSpline(self):
        degree = 3
        points = np.array([(2,4),(0,1),(6,5), (4,0)])
        self.helpTest(points,degree)
    def testNegativePointsSpline(self):
        degree = 3
        points = np.array([(-2,-4),(-1,-1),(-6,-5), (-4, -1)])
        self.helpTest(points,degree)
    #I don't understand the math enough to know if this test case is relevant
    def testEmptySpline(self):
        degree = 0
        points = np.array([])
        self.helpTest(points,degree)
    def testNegativeDegree(self):
        degree = -1
        points = np.array([])
        with self.assertRaises(ValueError):
            self.helpTest(points,degree)

if __name__=='__main__':
    ut.main()

