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


n =256 #n is the square lattice size
#s = 10000
s = int(math.ceil(n**2/4))/8
T = 2#Temperature
t_f = 1000 #total frames before end

""" Testing Code """

Lattice = LatticeMaker(n,s,0.01) #creates new lattice instance and names it lattice


"""Making Graphs"""



"""
### ANIMATIONS
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
#ani = animation.FuncAnimation(fig, Lattice.ReturnLatticeImage, interval=0.0001,blit='True',frames = t_f,repeat = False)
ani = animation.FuncAnimation(fig, Lattice.ReturnMagPlot, interval=0.0001,blit='True',frames = t_f,repeat = False)
#ani = animation.FuncAnimation(fig, Lattice.ReturnLatticeImage, interval=0.0001,blit='True',frames = t_f,repeat = False)
plt.xlabel('x-axis') #xaxis label
plt.ylabel('y-axis') #yaxis label
ax.set_title("Ising Model Simulation, Temperature = "+str(T), fontsize='large') #setting title

for tick in ax.xaxis.get_ticklabels(): #format x axis
    tick.set_fontsize('large')
    tick.set_fontname('Times New Roman')
    tick.set_color('blue')
    tick.set_weight('bold')
"""
###SUBPLOTS

#generating the 4 different lattices w different temperatures
Lattice = LatticeMaker(n,s,0.01) #creates new lattice instance and names it lattice

#evolves lattices in s steps using metropolis algorithm
for i in range(t_f):
    Lattice.Metropolis(i)
    
    
fig = plt.figure()
ax1 = fig.add_subplot(2, 2, 1)
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 1, 2)
plt.subplot_tool() #tools to reorganise subplots in figure
###formats axis labels to make them look better


ax1.imshow((Lattice.ReturnLattice()),origin = 'lower') #shows end product after manipulation
ax1.set_ylabel('Y') #sets x axis
ax1.set_xlabel('X') #sets y axis
ax2.grid(True)
ax2.xaxis.set_ticks(np.arange(-100, 1100, 200))
ax2.yaxis.set_ticks(np.arange(-120000, 0, 20000))
ax2.scatter(Lattice.t_list,Lattice.energy_list,s = 1)
ax2.set_ylabel('Energy') #sets x axis
ax2.set_xlabel('Time') #sets y axis

ax3.grid(True)
ax3.scatter(Lattice.t_list,Lattice.mag_list,s=3,color='red')
ax3.set_ylabel('Magnetisation') #sets x axis
ax3.set_xlabel('Time') #sets y axis


plt.show()
