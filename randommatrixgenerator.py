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
import isingfunctions as ifun

"""Creating New Lattice Class"""

class LatticeMaker: #LatticeMaker Class
    def __init__(self,n,s,T): #n = size of matrix
        self.n = n #assigns lattice size
        self.s = s #assigns number of steps per picture update
        self.T = T #assigns temperature of lattice
        self.matrix = ifun.RandomMatrix(self.n) #generates random matrix filled with 0,1. Doubles then -1 to get +-1 matrix

    def SetImage(self):
        self.image = plt.imshow(self.matrix,cmap = 'jet',interpolation = 'nearest',origin='lower') #image of lattice is updated as matrix.

    def RanSpinChange(self,i): #flips spin of random paticle. i is dummy variable
        for m in range(0,self.s): #loop step number times
            row = random.randint(0,self.n-1) #random row value
            col = random.randint(0,self.n-1) #random col value
            self.matrix[col,row] *= -1 #flips random row,col coordinate
        self.SetImage()
        return self.image, #image of lattice is returned to be in animation function

    def CheckSpins(self,row,col):
        
        spin = self.matrix[col,row]
        
        right = self.matrix[col,(row + 1) % self.n] #right = spin to right of random point in lattice
        left = self.matrix[col,(row - 1) % self.n] #left = spin to left of random point in lattice etc.
        up = self.matrix[(col - 1) % self.n,row] #Perioic Boundary conditions implemented. If point=lattice size
        down = self.matrix[(col + 1) % self.n,row] #this is then assigned 0. l[-1] is default last in list
        
        spinsum = right+left+up+down #spinsum is the sum of all adjacent spins from the random spin
        
        return spinsum    
    
    

    
    def Metropolis(self,i):
        for m in range(0,self.s): #loop step number times
            row = random.randint(0,self.n-1) #generates random row value
            col = random.randint(0,self.n-1) #generates random col value
            
            spinsum = self.CheckSpins(row,col)
            spin = self.matrix[col,row]        
            
            DeltaE = ifun.EnergyChange(spinsum,spin)
            
            self.matrix[col,row] *= ifun.SpinFlip(DeltaE,self.T)
            
        self.SetImage()
        return self.image, #image of lattice is returned to be in animation function
    
    def ReturnLattice(self): #returns matrix
        return self.matrix
    
    def PrintLattice(self): #prints matrix
        print self.matrix



"""Example"""
#LatticeNew = LatticeMaker(3) #creates new lattice type with n = 10
#LatticeNew.PrintLattice()
#RandomMatrix = LatticeNew.RandomLattice() #generates random matrix from n value

