# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:43:59 2017

@author: Cormac
"""

"""Importing Packages"""
import numpy as np
import random
import matplotlib.pyplot as plt

"""Creating New Lattice Class"""

class LatticeMaker: #LatticeMaker Class
    def __init__(self,n): #n = size of matrix
        self.n = n
        self.matrix = np.random.randint(2, size=(self.n,self.n))*2 -1 #object has attribute matrix which defines the spin lattice
    
    def RanSpinChange(self): #flips spin of random paticle. i is dummy variable 
        x = random.randint(0,self.n-1) #random x value
        y = random.randint(0,self.n-1) #random y value
        self.matrix[x,y] *= -1 #flips random x,y coordinate
    
    def ReturnLattice(self): #returns matrix
        return self.matrix
    
    def PrintLattice(self): #prints matrix
        print self.matrix

"""Example"""
#LatticeNew = LatticeMaker(3) #creates new lattice type with n = 10
#LatticeNew.PrintLattice()
#RandomMatrix = LatticeNew.RandomLattice() #generates random matrix from n value
