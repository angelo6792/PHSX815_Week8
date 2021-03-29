#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import math
import sympy as sp
from sympy import Symbol, integrate, exp, oo
from scipy.optimize import minimize
import matplotlib.pyplot as plt

xx = np.linspace(-1,1)

def f(x):
    return 8*x**4 - 4*x**2 + 3*x


plt.plot(xx,f(xx))
plt.show()

starting_guess = -3

print(minimize(f,[starting_guess]))
