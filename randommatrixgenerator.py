# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:43:59 2017

@author: Cormac
"""

"""Importing Packages"""
import numpy as np
import random

"""Creating New Lattice Class"""

class LatticeMaker:
    def __init__(self,n): #n = size of matrix
        self.n = n
    
    def RandomLattice(self): #method which creates random matrix
        return np.random.randint(2, size=(self.n,self.n))*2 -1 #creates new matrix full of 0s and 2s then subtracts 1
    
    def SpinChange(i): #flips spin of random paticle. i is dummy variable 
        x = random.randint(0,self.n-1) #random x value
        y = random.randint(0,self.n-1) #random y value
        lattice[x,y] *= -1 #flips random x,y coordinate

"""Example"""
#LatticeNew = LatticeMaker(10) #creates new lattice type with n = 10
#RandomMatrix = LatticeNew.RandomLattice() #generates random matrix from n value
