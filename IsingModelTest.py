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


### Assignment code for Tom Achers PY3P01 Assignment
### Creates a Ising Model Simulation Using Metropolis Algorithm
###
### USE: Keep sweep amount (s) at least 100 or program will run painfully slow
### MUST IMPORT "randommatrixgenerator.py" as a package. Almost all Functions used are methods of Lattice class
###


""" Defining Constants """

n = 80 #n is the square lattice size
s = 10000 #steps per picture update
T = 3. #Temperature

""" Testing Code """

Lattice = LatticeMaker(n,s) #creates new lattice instance and names it lattice

"""Making Graphs"""

fig = plt.figure() #creates new figure
ani = animation.FuncAnimation(fig, Lattice.RanSpinChange, interval=0.0001,blit='True')
ax = fig.add_subplot(1, 1, 1)

ax.set_title("Ising Model Simulation", fontsize='large') #setting title


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