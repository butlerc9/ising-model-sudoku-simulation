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
        self.mag_list = [0]
        self.magnetisation = 0
        self.energy = 0
        self.energy_list = [0]

        self.xmin,self.xmax = -1,25
        self.ymax = 600

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
    
    
    def Metropolis(self,i):#runs metropolis algorithm s times
        for m in range(0,self.s): #loop step number times
            row = random.randint(0,self.n-1) #generates random row value
            col = random.randint(0,self.n-1) #generates random col value
            
            spinsum = self.CheckSpins(row,col) #for random point check the spins of the adjacent lattice points
            spin = self.matrix[col,row] #check spin at random lattice point
            
            DeltaE = ifun.EnergyChange(spinsum,spin) #change in energy = -2*spin*spinsum*J
            
            Flip = ifun.SpinFlip(DeltaE,self.T) #multiply it by spinflip. = -1 if yes. = 1 if no.
            
            if Flip == -1:
                self.energy += DeltaE
            
            self.matrix[col,row] *= Flip
        print self.energy
        self.magnetisation = np.sum(self.ReturnLattice()) #calculates sum of the spins 
        self.mag_list.append(self.magnetisation)
        
    def ReturnLattice(self): #returns matrix
        return self.matrix
    
    def PrintLattice(self): #prints matrix
        print self.matrix
        
    def ReturnLatticeImage(self,i):
        self.Metropolis(i)
        self.image = plt.imshow(self.matrix,cmap = 'jet',interpolation = 'nearest',origin='lower') #image of lattice is updated as matrix. 
        return self.image, #image of lattice is returned to be in animation function
    
    def ReturnEnergyPlot(self,i):    
        self.Metropolis(i)
        self.image = plt.scatter(i,self.energy)
        plt.xlim(self.xmin,self.xmax)
        plt.ylim(-self.ymax,0)
        plt.grid(True)
        plt.xlabel("Time")
        plt.ylabel("Energy")
        if i > self.xmax:
            self.xmax *= 2
        if np.abs(self.energy) > self.ymax:
            self.ymax *= 2
        return self.image, #image of lattice is returned to be in animation function
        
        
    def ReturnMagPlot(self,i):
        self.Metropolis(i)
        self.image = plt.scatter(i,self.magnetisation)
        plt.xlim(self.xmin,self.xmax)
        plt.ylim(-self.ymax,self.ymax)
        plt.grid(True)
        plt.xlabel("Time")
        plt.ylabel("Magnetisation")
        if i > self.xmax:
            self.xmax *= 2
        if np.abs(self.magnetisation) > self.ymax:
            self.ymax *= 2
        return self.image, #image of lattice is returned to be in animation function

"""Example"""
#LatticeNew = LatticeMaker(3) #creates new lattice type with n = 10
#LatticeNew.PrintLattice()
#RandomMatrix = LatticeNew.RandomLattice() #generates random matrix from n value

