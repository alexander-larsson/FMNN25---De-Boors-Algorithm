import numpy as N

class Spline:

    def __init__(self,control_points,knots,degree):
        """
        Parameters:
        control_points = A list of control points
        knots = A list of knots
        degree = The degree of the B-spline
        """
        self.d = N.array(control_points)
        self.u = N.array(knots)
        self.p = degree

    def __call__(self,u):
        """Computes s(u)"""
        # Belov is the steps from 1.9 in slides
        # 1. Find hot interval
        i = (knots > u).argmax() # hot interval is [ui-1,ui]

        # 2. Select control points dI-3 ... dI (slides 1.9)
        # Slides say dI-2 ... dI+1 in many other places so I
        # assume this is correct instead.
        # Indexing gets weird because of the hot interval i is
        # + 1 over what it is on all the slides and python
        # slicing excludes the last index.
        # i is indexed from 0 in the slides.
        ctrl_pts = d[i-3:i+1]

        # 3. Run the blossom recursion


    def plot(self):
        """Plots the curve"""
        pass
