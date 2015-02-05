__author__ = 'Alex'


import numpy as np


class Function:

    def __init__(self, param=1):
        self.param = param

    def apply(self, x):
        return NotImplemented

    def apply_derivative(self, x):
        return NotImplemented

class Sigmoid(Function):

    def apply(self, x):
        return 1.0 / (1.0 + np.exp(-self.param * x))

    def apply_derivative(self, acts):
        return acts * (1 - acts)

class Linear(Function):

    def apply(self, x):
        return self.param * x

    def apply_derivative(self, x):
        return self.param
