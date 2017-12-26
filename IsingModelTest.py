# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 17:14:23 2017

@author: Cormac
"""
""" Importing Packages """
from randommatrixgenerator import LatticeMaker




""" Defining Constants """

n = 10 #n is the square lattice size


""" Testing Code """

New_Matrix = LatticeMaker(n) #creates new instance of latticemaker type with a given n
Lattice = New_Matrix.RandomLattice() #creates random matrix with nxn called lattice


"""Making Graphs"""