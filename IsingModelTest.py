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
s = int(math.ceil((n**2)))
T = 0.1#Temperature
t_f = 100 #total frames before end

""" Testing Code """

Lattice1 = LatticeMaker(n,s,0.001) #creates new lattice instance and names it lattice
Lattice2 = LatticeMaker(n,s,0.1) #creates new lattice instance and names it lattice

"""Making Graphs"""

fig = plt.figure() #creates new figure

ax = fig.add_subplot(1, 1, 1)

for i in range(t_f):
    Lattice1.Metropolis(i)
    Lattice2.Metropolis(i)

plt.scatter(range(t_f),Lattice1.energy_list)
plt.scatter(range(t_f),Lattice2.energy_list)



#ani = animation.FuncAnimation(fig, Lattice.ReturnEnergyPlot, interval=0.0001,blit='True',frames = t_f,repeat = False)
#ani = animation.FuncAnimation(fig, Lattice.ReturnMagPlot, interval=0.0001,blit='True',frames = t_f,repeat = False)
#ani = animation.FuncAnimation(fig, Lattice.ReturnLatticeImage,init_func=init, interval=0.0001,blit='True',frames = t_f,repeat = False)

ax.set_title("Ising Model Simulation", fontsize='large') #setting title

###formats axis labels to make them look better
for tick in ax.xaxis.get_ticklabels(): #format x axis
    tick.set_fontsize('large')
    tick.set_fontname('Times New Roman')
    tick.set_color('blue')
    tick.set_weight('bold')

for tick in ax.yaxis.get_ticklabels(): #format y axis
    tick.set_fontsize('large')
    tick.set_fontname('Times New Roman')
    tick.set_color('blue')
    tick.set_weight('bold')

plt.xlabel('x-axis') #xaxis label
plt.ylabel('y-axis') #yaxis label

plt.show()
