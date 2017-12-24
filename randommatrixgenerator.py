# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 16:43:59 2017

@author: Cormac
"""

"""Importing Packages"""
import numpy as np


"""Creating New Lattice Class"""

class Lattice:
    def __init__(self,n): #n = size of matrix
        self.n = n
    
    def RandomLattice(self): #method which creates random matrix
        return np.random.randint(2, size=(self.n,self.n))*2 -1 #creates new matrix full of 0s and 2s then subtracts 1

"""Example"""
LatticeNew = Lattice(10) #creates new lattice type with n = 10
RandomMatrix = LatticeNew.RandomLattice() #generates random matrix from n value