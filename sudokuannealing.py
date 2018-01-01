# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:26:29 2017

@author: Cormac
"""

### Sudoku Solver Via Simulated Annealing
### Cormac Butler PY3C01 Assignment
###
### IMPORTANT although the notation refers to the sudoku puzzle as a "matrix" in the code
### it is stored as a list. This greatly simplifies arithmitic e.g. Columns are just 9 away in list etc.
### 
### Many Valuable Pieces of code were adapted from: https://github.com/erichowens/SudokuSolver/blob/master/sudoku.py
###
### When inputting puzzle, all empty values should be entered as Zeros, which are
### odviously not present in a normal sudoku puzzle.


"""Importing Packages"""
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import sys
from random import shuffle, random, sample, randint
import matplotlib.patches as mpatches

"""Creating Sudoku Class Lattice Class"""

class SudokuMaker: # initialises Sudoku Making Class
    def __init__(self):
        self.nonfixed = [] #initialises list of indexs of 
        self.score = 0 #initialises score
        self.T = .5
        self.count = 0
        self.win = 0
        self.energies = []
        self.counts = []
        self.win = False
    
    def MatrixAssign(self,matrix): #takes list as argument and calls it it self.matrix
        self.matrix = matrix
        for i in range(len(self.matrix)): #finds all zeros in puzzle and adds them to movable list
            if self.matrix[i] == 0:
                self.nonfixed.append(i)
    
    
    
    def PrintPuzzle(self): #print as list
        print np.reshape(self.matrix, (9, 9))
    
    def ReturnPuzzle(self): #returns as list
        return self.matrix
        
    
    def GetCol(self,x): #returns values of column x (0-8)
        col_values = []
        for i in range(9):
            col_values.append(self.matrix[x+i*9])
        return col_values

    def GetRow(self,y): #returns values of row y (0-8)
        row_values = []
        for i in range(9):
            row_values.append(self.matrix[9*y+i])
        return row_values
    
    def GetBoxi(self,b): #gets all indexs in the bth box. Indexs wrap from right to left.
        row_offset = (b // 3) * 3
        col_offset = (b % 3)  * 3
        indices = [col_offset + (j%3) + 9*(row_offset + (j//3)) for j in range(9)]
        return indices
    
    def GetBoxV(self,b): #returns all values of numbers within the box
        box_values = []
        for i in self.GetBoxi(b):
            box_values.append(self.matrix[i])
        return box_values
    
    def RandomiseZeros(self): #takes puzzle and inputs all randomised numbers. Makes sure each box contains 1-9
        for b in range(9): #for each box
            indices = self.GetBoxi(b) #get indices of each box
            movable_indices = list( set(indices) & set(self.nonfixed)) #intersection (indexes in box )&(Non fixed number indexs)
            nums = [i for i in range(1,10) if i not in set(self.GetBoxV(b))] #Values of numbers not already in box
            shuffle(nums) #rearrange numbers so the arent chronological
            for i in range(len(nums)): #for each number in nums
                index = movable_indices[i]
                self.matrix[index] = nums[i] #replace zero with new value from num
    
    def GetEnergy(self): # Energy = sum of uniques row +columns Max = every number is a same e.g. all 1s => Energy = 162
        rowcount = 0
        colcount = 0
        for i in range(9):
            rowcount += len(set(self.GetRow(i)))
            colcount += len(set(self.GetCol(i)))
        self.Energy = 162 - rowcount - colcount 
        return self.Energy
    
    def SwapEntries(self,i1,i2):
        v1 = self.matrix[i1]
        v2 = self.matrix[i2]
        self.matrix[i1] = v2
        self.matrix[i2] = v1
    
    
    
    def Metropolis(self):
        
        box_number = randint(0,8) #picks random box
        indices = self.GetBoxi(box_number) #gets box indices
        movable_indices = list( set(indices) & set(self.nonfixed)) #gets movable box indices
        shuffle(movable_indices)
        i1 = movable_indices[0]
        i2 = movable_indices[1]
        
        Energy_old = self.GetEnergy()
        self.SwapEntries(i1,i2)
        Energy_new = self.GetEnergy()
        DeltaE = Energy_old - Energy_new
        self.SwapEntries(i1,i2)
        if Energy_new <= Energy_old:
            self.SwapEntries(i1,i2)
        elif np.random.random() <= np.exp(float(DeltaE/self.T)):
            #print Energy_old,Energy_new,'up'
            self.SwapEntries(i1,i2)
        
        
        
        
        if (self.count % 1000) == 0:
            print "count:",self.count,"Energy:",Energy_new, "Temperature:", self.T
            self.T *= 0.99
            self.energies.append(Energy_new)
            self.counts.append(self.count)
            
            
        if self.Energy == 0:
            print "Winner!!!! Solution:"
            print "final count:",self.count, "Temperature:", self.T
            print np.reshape(self.ReturnPuzzle(), (9, 9))
            self.win = 1
            self.energies.append(Energy_new)
            self.counts.append(self.count)
            self.win = True
        self.count += 1
        
    def PlotEnergy(self):
        plt.plot(self.counts,self.energies)
            
        

""" Puzzle Input AS LIST """

PuzzleTemplate = np.array(       [0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0,
                                  0,0,0,0,0,0,0,0,0])

PuzzleEasy = np.array(           [7,9,0,0,0,0,3,0,0,
                                  0,0,0,0,0,6,9,0,0,
                                  8,0,0,0,3,0,0,7,6,
                                  0,0,0,0,0,5,0,0,2,
                                  0,0,5,4,1,8,7,0,0,
                                  4,0,0,7,0,0,0,0,0,
                                  6,1,0,0,9,0,0,0,8,
                                  0,0,2,3,0,0,0,0,0,
                                  0,0,9,0,0,0,0,5,4])
#WebLink: https://www.sudoku.ws/easy-1.htm


PuzzleStandard = np.array(       [0,0,5,0,9,0,0,0,1,
                                  0,0,0,0,0,2,0,7,3,
                                  7,6,0,0,0,8,2,0,0,
                                  0,1,2,0,0,9,0,0,4,
                                  0,0,0,2,0,3,0,0,0,
                                  3,0,0,1,0,0,9,6,0,
                                  0,0,1,9,0,0,0, 5,8,
                                  9,7,0,5,0,0,0,0,0,
                                  5,0,0,0,3,0,7,0,0])
#WebLink: https://www.sudoku.ws/standard-1.htm

PuzzleHard = np.array(           [0,0,0,2,0,0,0,6,3,
                                  3,0,0,0,0,5,4,0,1,
                                  0,0,1,0,0,3,9,8,0,
                                  0,0,0,0,0,0,0,9,0,
                                  0,0,0,5,3,8,0,0,0,
                                  0,3,0,0,0,0,0,0,0,
                                  0,2,6,3,0,0,5,0,0,
                                  5,0,3,7,0,0,0,0,8,
                                  4,7,0,0,0,1,0,0,0])
#WebLink: https://www.sudoku.ws/hard-1.htm

""" Testing Code """
M_Visual = np.reshape(np.arange(0,81,1), (9, 9)) #generates a 9x9 matrix. Helps to visualise where indexs are

def SolvePuzzle(Puzzle,plot):
    Sudoku = SudokuMaker() #creates SudokuMaker Instance
    
    Sudoku.MatrixAssign(Puzzle) #inserts puzzle
    print "original puzzle: (0 implies empty slot)"
    Sudoku.PrintPuzzle()
    Sudoku.RandomiseZeros() #randomises zeros in each box from 1-9
    for i in range(50001):
        Sudoku.Metropolis()
        if Sudoku.win == 1:
            break
    if plot == 'yes':
        if Sudoku.win == True:
            color1 = 'green'
            color2 = 'blue'
            
        else :
            color1 = 'red'
            color2 = 'pink'
        
        plt.plot(Sudoku.counts,Sudoku.energies,color = color1)
        plt.scatter(Sudoku.count,Sudoku.Energy,s=80, facecolors=color2, edgecolors=color1)
    

""" Solving Puzzle """

red_patch = mpatches.Patch(color='red', label='Unsuccessful Solve')
blue_patch = mpatches.Patch(color='green', label='Successful Solve')
plt.legend(handles=[red_patch, blue_patch], prop={'size': 26})

plt.grid(True)
plt.xlabel('Iterations') #xaxis label
plt.ylabel('Energy') #yaxis label

SolvePuzzle(PuzzleEasy,'yes')

#plt.imshow(Display,interpolation = 'nearest',origin = 'lower',cmap = 'jet')
