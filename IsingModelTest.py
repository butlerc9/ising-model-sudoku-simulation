# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 17:14:23 2017

@author: Cormac
"""
""" Importing Packages """
from randommatrixgenerator import LatticeMaker
import numpy as np
import random
import matplotlib.pyplot as plt



""" Defining Constants """

n = 128#n is the square lattice size


""" Testing Code """

Lattice = LatticeMaker(n)
Lattice.PrintLattice()
Lattice.RanSpinChange()
Lattice.RanSpinChange()
Lattice.RanSpinChange()
Lattice.PrintLattice()


im = plt.imshow(Lattice.ReturnLattice(), animated=True,cmap = 'cool',interpolation = 'bilinear')



"""Making Graphs"""