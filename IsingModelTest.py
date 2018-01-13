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
import matplotlib.patches as mpatches

### Assignment code for Tom Achers PY3P01 Assignment
### Creates a Ising Model Simulation Using Metropolis Algorithm
###
### USE: Keep sweep amount (s) at least 100 or program will run painfully slow
### MUST IMPORT "randommatrixgenerator.py" as a package. Almost all Functions 
### used are methods of Lattice class
### Close Figures to open future ones to prevent crashes
### Comment

""" Defining Constants """

n =64. #n is the square lattice size
s = 1000000
T = 1.#Temperature
t_f = 1#total frames before end

""" Testing Code """

"""Making Graphs"""

fig = plt.figure() #creates new figure

ax = fig.add_subplot(1, 1, 1)

def AnnealPlot(T0): #plot energy of annealed lattice
    Lattice = LatticeMaker(n,s,T0) #creates new lattice instance and names it lattice
    for i in range(t_f):
        Lattice.Metropolis(i,'yes',t_f)
    plt.plot(range(t_f),Lattice.energy_list,color = 'blue')

def NonAnnealPlot(): # plots energy
    Lattice2 = LatticeMaker(n,s,0.000000001) #creates new lattice instance and names it lattice
    for i in range(t_f):
        Lattice2.Metropolis(i,'no',t_f)
    plt.plot(range(t_f),Lattice2.energy_list, linewidth = 1,linestyle = '--',color = 'red')

#for i in range(1):
#    AnnealPlot(1)

###Generates Legend
red_patch = mpatches.Patch(color='red', label='Non Annealed')
blue_patch = mpatches.Patch(color='blue', label='Annealed')
plt.legend(handles=[red_patch, blue_patch], prop={'size': 26})

Lattice = LatticeMaker(n,s,T)

#ani = animation.FuncAnimation(fig, Lattice.ReturnEnergyPlot, interval=0.0001,blit='True',frames = t_f,repeat = False)
#ani = animation.FuncAnimation(fig, Lattice.ReturnMagPlot, interval=0.0001,blit='True',frames = t_f,repeat = False)
ani = animation.FuncAnimation(fig, Lattice.ReturnLatticeImage,init_func=init, interval=0.0001,blit='True',frames = t_f,repeat = False)

ax.set_title("Annealing Simulation of 2D Spin Lattice, N = 64", fontsize='large') #setting title

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

plt.xlabel('Frames') #xaxis label
plt.ylabel('Energy per Particle (E/N^2)') #yaxis label

plt.show()
