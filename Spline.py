#http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/de-Boor.html

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
        i = (self.knots > self.u).argmax() # hot interval is [ui-1,ui]

        # 2. Select control points dI-3 ... dI (slides 1.9)
        # Slides say dI-2 ... dI+1 in many other places so I
        # assume this is correct instead.
        # Indexing gets weird because of the hot interval i is
        # + 1 over what it is on all the slides and python
        # slicing excludes the last index.
        # i is indexed from 0 in the slides.
        ctrl_pts = self.d[i-3:i+1]

        # 3. Run the blossom recursion
        # Has to figure out how many knots we need here
        su = self.blossom_recursion(u,ctrl_pts,knots)


    def __createAlpha__(self,u):
        """
        Creates an alpha function with fixed u
        Parameters:
        u = The u for wich we are evaluating s(u)
        """
        def alpha(self,ur,ul):
            """
            Parameters:
            ur = The rightmost knot
            ul = The leftmost knot
            """
            return (ur-u)/(ur-ul)
        return alpha

    def blossom_recursion(self,u,control_points,knots):
        if not knots:
            return control_points[0]
        else:
            gap = len(knots)/2
            leftmost = knots[:gap]
            rightmost = knots[gap:]
            alpha = self.__createAlpha__(u)
            alphas = N.array([ alpha(a,b) for (a,b) in zip(rightmost,leftmost) ])
            new_control_points = N.zeros((1, control_points.size - 1))

            for i in range(new_control_points.size):
                a = alphas[i]
                new_control_points[i] = a*control_points[i] + (a - 1)control_points[i+1]

            return blossom_recursion(new_control_points,knots[1:-1])


    def plot(self):
        """Plots the curve"""
        pass
