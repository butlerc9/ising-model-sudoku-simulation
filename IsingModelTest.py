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
### Comment

""" Defining Constants """


n =64 #n is the square lattice size
s = 10000
T = 2#Temperature
t_f = 10 #total frames before end

""" Testing Code """

Lattice = LatticeMaker(n,s,0.01) #creates new lattice instance and names it lattice


"""Making Graphs"""



"""
### ANIMATIONS
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ani = animation.FuncAnimation(fig, Lattice.ReturnLatticeImage, interval=0.0001,blit='True',frames = t_f,repeat = False)
#ani = animation.FuncAnimation(fig, Lattice.ReturnMagPlot, interval=0.0001,blit='True',frames = t_f,repeat = False)
#ani = animation.FuncAnimation(fig, Lattice.ReturnLatticeImage, interval=0.0001,blit='True',frames = t_f,repeat = False)
plt.xlabel('x-axis') #xaxis label
plt.ylabel('y-axis') #yaxis label
ax.set_title("Ising Model Simulation, Temperature = "+str(T), fontsize='large') #setting title

for tick in ax.xaxis.get_ticklabels(): #format x axis
    tick.set_fontsize('large')
    tick.set_fontname('Times New Roman')
    tick.set_color('blue')
    tick.set_weight('bold')

###SUBPLOTS
"""
#generating the 4 different lattices w different temperatures
Lattice1 = LatticeMaker(n,s,0.01) #creates new lattice instance and names it lattice
Lattice2 = LatticeMaker(n,s,1.5) #creates new lattice instance and names it lattice
Lattice3 = LatticeMaker(n,s,2.5) #creates new lattice instance and names it lattice
Lattice4 = LatticeMaker(n,s,5.) #creates new lattice instance and names it lattice

#evolves lattices in s steps using metropolis algorithm
for i in range(t_f):
    Lattice1.Metropolis(0)
    Lattice2.Metropolis(0)
    Lattice3.Metropolis(0)
    Lattice4.Metropolis(0)
    
    
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
plt.subplot_tool() #tools to reorganise subplots in figure
###formats axis labels to make them look better


ax1.imshow((Lattice1.ReturnLattice()),origin = 'lower') #shows end product after manipulation
ax1.set_title('Temperature = 0.01', fontsize=15) #sets title of subplot
ax1.set_ylabel('Y') #sets x axis
ax1.set_xlabel('X') #sets y axis

ax2.imshow((Lattice2.ReturnLattice()),origin = 'lower')
ax2.set_title('Temperature = 1.5', fontsize=15)
ax2.set_ylabel('Y')
ax2.set_xlabel('X')

ax3.imshow((Lattice3.ReturnLattice()),origin = 'lower')
ax3.set_title('Temperature = 2.5', fontsize=15)
ax3.set_ylabel('Y')
ax3.set_xlabel('X')

ax4.imshow((Lattice4.ReturnLattice()),origin = 'lower')
ax4.set_title('Temperature = 2.5', fontsize=15)
ax4.set_ylabel('Y')
ax4.set_xlabel('X')

plt.show()
