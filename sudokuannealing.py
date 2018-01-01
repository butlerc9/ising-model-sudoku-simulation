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

"""Creating Sudoku Class Lattice Class"""

class SudokuMaker: # initialises Sudoku Making Class
    def __init__(self):
        self.nonfixed = [] #initialises list of indexs of 
        self.score = 0 #initialises score
    
    def MatrixAssign(self,matrix): #takes list as argument and calls it it self.matrix
        self.matrix = matrix
        for i in range(len(self.matrix)): #finds all zeros in puzzle and adds them to movable list
            if self.matrix[i] == 0:
                self.nonfixed.append(i)

    def PrintPuzzle(self): #print as list
        print self.matrix
    
    def ReturnPuzzle(self): #returns as list
        return self.matrix
        
    
    def GetCol(self,x): #returns values of column x (0-8)
        col_values = []
        for i in range(9):
            col_values.append(self.matrix[x+i*9])
        return col_values

    def GetRow(self,y): #returns values of row y (0-8)
        row_values = []
        row_values.append(self.matrix[9*y:9*y+9])
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
        

""" Puzzle Input AS LIST """

Puzzle = np.array(               [5,3,0,0,0,0,0,0,0,
                                  6,0,0,1,0,5,0,0,0,
                                  0,9,8,0,0,0,0,6,0,
                                  8,0,0,0,6,0,0,0,3,
                                  4,0,0,8,0,3,0,0,0,
                                  7,0,0,0,2,0,0,0,6,
                                  0,6,0,0,0,0,2,8,0,
                                  0,0,0,4,1,9,0,0,5,
                                  0,0,0,0,8,0,0,7,9])


""" Testing Code """
M_Visual = np.reshape(np.arange(0,81,1), (9, 9)) #generates a 9x9 matrix. Helps to visualise where indexs are

Sudoku = SudokuMaker() #creates SudokuMaker Instance
Sudoku.MatrixAssign(Puzzle) #inserts puzzle
Sudoku.RandomiseZeros() #randomises zeros in each box from 1-9

#Display = np.reshape(Sudoku.ReturnPuzzle(), (9, 9))
#plt.imshow(Display,interpolation = 'nearest',origin = 'lower',cmap = 'jet')
