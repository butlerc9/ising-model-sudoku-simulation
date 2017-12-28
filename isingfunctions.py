# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 00:58:18 2017

@author: Cormac
"""

import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import sys

### Functions for Miscelaneous Use in Simulation
###
###
### 
###
###
### 

def RandomMatrix(n): #generates random n sized matrix
     matrix = np.random.randint(2, size=(n,n))*2 -1 #generates random matrix filled with 0,1. Doubles then -1 to get +-1 matrix
     return matrix


def EnergyChange(spinsum,spin): #takes particle spin and adjacent spin sum returns energy change value
    J = 1 #coupling constant J set to be 1
    DeltaE = -2*spin*spinsum*J
    return DeltaE