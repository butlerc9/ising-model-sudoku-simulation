# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:26:29 2017

@author: Cormac
"""

"""Importing Packages"""
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import sys
from random import shuffle, random, sample, randint

"""Creating Sudoku Class Lattice Class"""

class SudokuMaker:
    def __init__(self):
        self.nonfixed = []
        self.score = 0
    
    def MatrixAssign(self,matrix):
        self.matrix = matrix
        for i in range(len(self.matrix)):
            if self.matrix[i] == 0:
                self.nonfixed.append(i)

    def PrintPuzzle(self):
        print self.matrix
    
    def ReturnPuzzle(self):
        return self.matrix
        
    
    def GetCol(self,x):
        col_values = []
        for i in range(9):
            col_values.append(self.matrix[x+i*9])
        return col_values

    def GetRow(self,y):
        row_values = []
        row_values.append(self.matrix[9*y:9*y+9])
        return row_values
    
    def GetBoxi(self,b):
        row_offset = (b // 3) * 3
        col_offset = (b % 3)  * 3
        indices = [col_offset + (j%3) + 9*(row_offset + (j//3)) for j in range(9)]
        return indices
    
    def GetBoxV(self,b):
        box_values = []
        for i in self.GetBoxi(b):
            box_values.append(self.matrix[i])
        return box_values
    
    def RandomiseZeros(self):
        for b in range(9):
            indices = self.GetBoxi(b)
            movable_indices = list( set(indices) & set(self.nonfixed))
            nums = [i for i in range(1,10) if i not in set(self.GetBoxV(b))]
            shuffle(nums)
            for i in range(len(nums)):
                index = movable_indices[i]
                self.matrix[index] = nums[i]
        

""" Testing Code """

Puzzle = np.array(               [5,3,0,0,0,0,0,0,0,
                                  6,0,0,1,0,5,0,0,0,
                                  0,9,8,0,0,0,0,6,0,
                                  8,0,0,0,6,0,0,0,3,
                                  4,0,0,8,0,3,0,0,0,
                                  7,0,0,0,2,0,0,0,6,
                                  0,6,0,0,0,0,2,8,0,
                                  0,0,0,4,1,9,0,0,5,
                                  0,0,0,0,8,0,0,7,9])


M_Visual = np.reshape(np.arange(0,81,1), (9, 9))

Sudoku = SudokuMaker()
Sudoku.MatrixAssign(Puzzle)



nums = [i for i in range(1,13) if i not in set(Sudoku.matrix)]

Sudoku.RandomiseZeros()
Display = np.reshape(Sudoku.ReturnPuzzle(), (9, 9))
