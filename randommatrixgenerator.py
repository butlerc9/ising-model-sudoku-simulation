# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:43:59 2017

@author: Cormac
"""


"""Importing Packages"""
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import sys

"""Creating New Lattice Class"""

class LatticeMaker: #LatticeMaker Class
    
    def __init__(self,n,s): #n = size of matrix
        self.n = n #assigns lattice size
        self.s = s #assigns number of steps per picture update
        self.matrix = np.random.randint(2, size=(self.n,self.n))*2 -1 #generates random matrix filled with 0,1. Doubles then -1 to get +-1 matrix

    
    def RanSpinChange(self,i): #flips spin of random paticle. i is dummy variable
        for m in range(1,self.s): #loop step number times
            x = random.randint(0,self.n-1) #random x value
            y = random.randint(0,self.n-1) #random y value
            self.matrix[x,y] *= -1 #flips random x,y coordinate
        self.image = plt.imshow(self.matrix,cmap = 'jet',interpolation = 'nearest',origin='lower') #image of lattice is updated as matrix.
        return self.image, #image of lattice is returned to be in animation function
    
    def ReturnLattice(self): #returns matrix
        return self.matrix
    
    def PrintLattice(self): #prints matrix
        print self.matrix
    
    
"""Example"""
#LatticeNew = LatticeMaker(3) #creates new lattice type with n = 10
#LatticeNew.PrintLattice()
#RandomMatrix = LatticeNew.RandomLattice() #generates random matrix from n value

