import numpy as np
from sympy import *

#import sectionA as sp
class Exo1():
    def __init__(self):
        super().__init__()

        self.k = symbols("k")
        self.x = symbols("x")
        self.Y = (sin(self.x * self.k ** 2) / (self.k ** 5))

    def pathological_function(self):
        summ = summation(self.Y, (self.k, 1, 100))
        return summ

    def derivatives(self):
        expr = self.Y.subs(self.x, 1)
        difK = diff(expr, self.k)
        dif2K = diff(difK, self.k)
        result = [difK, dif2K]
        plot(difK, (self.k, 0.5, 100), title="Exo Graph", xlabel='k', ylabel="dy/dk", legend=True, line_color="blue")
        plot(dif2K, (self.k, 0.5, 100), title="Exo Graph (Second Derivative)", xlabel='k', ylabel="d^2Y/dk^2",
             legend=True, line_color="red")
        return result

E = Exo1()
#A = E.pathological_function()
B = E.derivatives()
#print(A)
print(B)
