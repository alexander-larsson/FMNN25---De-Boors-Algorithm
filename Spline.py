#http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/spline/de-Boor.html

import numpy as N
import matplotlib.pyplot as plt

class Spline:
    def __init__(self,control_points,degree):
        """
        Parameters:
        control_points = A list of control points
        degree = The degree of the B-spline
        """
        self.d = N.array(control_points)
        self.p = degree
        # Caluclate the knots we need
        # p 0 knots -> lin space -> p 1 knots
        start = N.zeros((1,degree))[0]
        nbr_internal_knots = len(control_points)-degree+1
        middle = N.linspace(0.0, 1.0, num=nbr_internal_knots)
        end = N.ones((1,degree))[0]
        self.u = N.concatenate((start,middle,end))


    def __call__(self,u):
        """Computes s(u)"""
        # Belov is the steps from 1.9 in slides
        # 1. Find hot interval
        i = (self.u >= u).argmax() # hot interval is [ui-1,ui]

        # 2. Select control points dI-3 ... dI (slides 1.9)
        # Slides say dI-2 ... dI+1 in many other places but
        # it seems  dI-3 ... dI works.
        # Indexing gets weird because of the hot interval i is
        # + 1 more than what it is on all the slides and python
        # slicing excludes the last index.
        # i is indexed from 0 in the slides.
        ctrl_pts = self.d[i-4:i+1]

        # 3. Run the blossom recursion
        knots = self.u[i-3:i+3]
        su = self.__blossom_recursion__(u,ctrl_pts,knots)
        return su


    def __createAlpha__(self,u):
        """
        Creates an alpha function with fixed u
        Parameters:
        u = The u for wich we are evaluating s(u)
        """
        def alpha(ur,ul):
            """
            Parameters:
            ur = The rightmost knot
            ul = The leftmost knot
            """
            return (ur-u)/(ur-ul)
        return alpha

    def __blossom_recursion__(self,u,control_points,knots):
        if knots.size == 0:
            return control_points[0]
        else:
            gap = len(knots)/2
            leftmost = knots[:gap]
            rightmost = knots[gap:]
            alpha = self.__createAlpha__(u)
            alphas = N.array([ alpha(a,b) for (a,b) in zip(rightmost,leftmost) ])
            new_control_points = N.zeros((control_points.size//2 - 1, 2))
            for i in range(new_control_points.size//2):
                a = alphas[i]
                new_control_points[i] = a*control_points[i] + (1-a)*control_points[i+1]
            return self.__blossom_recursion__(u,new_control_points,knots[1:-1])


    def plot(self,plot_control_polygon):
        """
        Plots the curve
        Parameters:
        plot_control_polygon = The control polygon will be plotted if this is True
        """
        u_values = N.linspace(0.0, 1.0, num=100)
        # Mapping over self means mapping over self.__call__
        points = N.array(list(map(self,u_values)))
        # This print shows that the last point is wrong
        # Should be [1,0] but is [0,0]
        x_points = [x for [x, y] in points]
        y_points = [y for [x, y] in points]
        plt.plot(x_points,y_points)
        if plot_control_polygon:
            x_ctrl_pts = [x for [x, y] in self.d]
            y_ctrl_pts = [y for [x, y] in self.d]
            plt.plot(x_ctrl_pts,y_ctrl_pts,'ro-')
        plt.ylabel('Super awesome B-spline')
        plt.show()

# Some code that tests the program
cp = [(0,0),(0,1),(1,1),(1,0)]
degree = 3
s = Spline(cp,degree)
s.plot(True)
