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
import matplotlib.animation as animation
import sys
import matplotlib as mpl
import math


### Assignment code for Tom Achers PY3P01 Assignment
### Creates a Ising Model Simulation Using Metropolis Algorithm
###
### USE: Keep sweep amount (s) at least 100 or program will run painfully slow
### MUST IMPORT "randommatrixgenerator.py" as a package. Almost all Functions 
### used are methods of Lattice class
### Close Figures to open future ones to prevent crashes

""" Defining Constants """

n = 64 #n is the square lattice size
s = 50000 # steps before end of picture
T = 0.1#Temperature
t_f = 100 #total frames before end

""" Testing Code """

#generating the 4 different lattices w different temperatures
Lattice1 = LatticeMaker(n,s,0.01) #creates new lattice instance and names it lattice
Lattice2 = LatticeMaker(n,s,1.5) #creates new lattice instance and names it lattice
Lattice3 = LatticeMaker(n,s,2.5) #creates new lattice instance and names it lattice
Lattice4 = LatticeMaker(n,s,5.) #creates new lattice instance and names it lattice

#evolves lattices in s steps using metropolis algorithm
Lattice1.Metropolis(0)
Lattice2.Metropolis(0)
Lattice3.Metropolis(0)
Lattice4.Metropolis(0)

"""Making Graphs"""

fig, axs = plt.subplots(2, 2) #generates 2x2 subplot grid

axs[0, 0].imshow((Lattice1.ReturnLattice()),origin = 'lower') #shows end product after manipulation
axs[0, 0].set_title('Temperature = 0.01', fontsize=15) #sets title of subplot
axs[0,0].set_ylabel('Y') #sets x axis
axs[0,0].set_xlabel('X') #sets y axis

axs[0, 1].imshow((Lattice2.ReturnLattice()),origin = 'lower')
axs[0, 1].set_title('Temperature = 1.5', fontsize=15)
axs[0,1].set_ylabel('Y')
axs[0,1].set_xlabel('X')

axs[1, 0].imshow((Lattice3.ReturnLattice()),origin = 'lower')
axs[1, 0].set_title('Temperature = 2.5', fontsize=15)
axs[1,0].set_ylabel('Y')
axs[1,0].set_xlabel('X')

axs[1, 1].imshow((Lattice4.ReturnLattice()),origin = 'lower')
axs[1, 1].set_title('Temperature = 5', fontsize=15)
axs[1,1].set_ylabel('Y')
axs[1,1].set_xlabel('X')

plt.subplot_tool() #tools to reorganise subplots in figure
plt.show()

