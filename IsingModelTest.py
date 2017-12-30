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

n =128 #n is the square lattice size
s = int(math.ceil((n**2)/4))
T = 0.1#Temperature
t_f = 100 #total frames before end

""" Testing Code """

Lattice = LatticeMaker(n,s,T) #creates new lattice instance and names it lattice

"""Making Graphs"""

fig = plt.figure() #creates new figure

ax = fig.add_subplot(1, 1, 1)
ani = animation.FuncAnimation(fig, Lattice.ReturnLatticeImage, interval=0.0001,blit='True',frames = t_f,repeat = False)
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
