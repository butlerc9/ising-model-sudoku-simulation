# -*- coding: utf-8 -*-
"""
Created on Sun Dec 31 19:26:29 2017

@author: Cormac
"""

### Sudoku Solver Via Simulated Annealing
### Cormac Butler PY3C01 Assignment 2017/18
###
### IMPORTANT although the notation refers to the sudoku puzzle as a "matrix" in the code
### it is stored as a list. This greatly simplifies arithmitic e.g. Columns are just 9 away in list etc.
### when plotting the list it is reshaped as a matrix.
### 
### Many Valuable Pieces of code were adapted from: https://github.com/erichowens/SudokuSolver/blob/master/sudoku.py
###
### When inputting puzzle, all empty values should be entered as Zeros, which are
### odviously not present in a normal sudoku puzzle.
### Instead of importing the Sudoku puzzles from a seperate module I wanted the code to be immediately
### Ready to run and as such the puzzles themselves are included here


"""Importing Packages"""
import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl
import sys
from random import shuffle, random, sample, randint
import matplotlib.patches as mpatches
import copy

"""Creating Sudoku Class Lattice Class"""

class SudokuMaker: # initialises Sudoku Making Class
    def __init__(self,anneal = None,T0 = None): #initialization function
        self.nonfixed = [] #initialises list of non-fixed indexes that can be changed in Puzzle
        self.score = 0 #initialises score
        if anneal == None:
            self.anneal = 'no'
        else:
            self.anneal = anneal
            
            
            
        if self.anneal == 'no' and T0 == None: 
            self.T = .000001 #sets non annealing temp at value very close to zero
        elif self.anneal == 'no' and T0 != None:
            self.T = T0
        else:
            self.T = T0
        self.count = 0 #initialises iteration count
        self.win = False # initialises win variable (True/False)
        self.energies = [] #Table of calculated energies
        self.counts = [] #list of counts at which solutions are found
        self.wincount = 0 #number of wins
    
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
        col_values = [] #create empty list
        for i in range(9): #for every column
            col_values.append(self.matrix[x+i*9]) #column values are multiples of 9
        return col_values #return column list values

    def GetRow(self,y): #returns values of row y (0-8)
        row_values = [] #create empty list
        for i in range(9): #for every column
            row_values.append(self.matrix[9*y+i]) #row values are 9 consecutive values every 9th entry
        return row_values #return row list values
    
    def GetBoxi(self,b): #gets all indexs in the bth box. Indexs wrap from right to left of matrix
        row_offset = (b // 3) * 3 #floor divides b by 3 to group top 3 middle 3 and bottom 3 together. Then multiplies by 3 to get the first row of the box
        col_offset = (b % 3)  * 3
        indices = [col_offset + (j%3) + 9*(row_offset + (j//3)) for j in range(9)] #cycles through 3 values then goes down a row
        return indices #returns box indices
    
    def GetBoxV(self,b): #returns all values of numbers within the box
        box_values = [] #creates new box values list
        for i in self.GetBoxi(b): #for i in box b indices
            box_values.append(self.matrix[i])
        return box_values #return values of box b
    
    def RandomiseZeros(self): #takes puzzle and inputs all randomised numbers. Makes sure each box contains 1-9
        for b in range(9): #for each box
            indices = self.GetBoxi(b) #get indices of each box
            self.movable_indices = list( set(indices) & set(self.nonfixed)) #intersection (indexes in box )&(Non fixed number indexs)
            nums = [i for i in range(1,10) if i not in set(self.GetBoxV(b))] #Values of numbers not already in box
            shuffle(nums) #rearrange numbers so the arent chronological
            for i in range(len(nums)): #for each number in nums
                index = self.movable_indices[i]
                self.matrix[index] = nums[i] #replace zero with new value from num
    
    def GetEnergy(self): # Energy = sum of uniques row +columns Max = every number is a same e.g. all 1s => Energy = 162
        rowcount = 0 #number of non-unique entries per row
        colcount = 0 #number of non-unique entries per column
        for i in range(9): #go through 9 rows and columns
            rowcount += len(set(self.GetRow(i))) #add to score any errors/nonunique values
            colcount += len(set(self.GetCol(i)))
        self.Energy = 162 - rowcount - colcount #max energy (all 1 value = 162) so we subtract from this so ground state energy = 0
        return self.Energy #returns current energy of system
    
    def SwapEntries(self,i1,i2): #swaps two entries of puzzle given indices i1,i2
        v1 = self.matrix[i1]
        v2 = self.matrix[i2]
        self.matrix[i1] = v2
        self.matrix[i2] = v1
    
    
    
    def Metropolis(self):
        
        box_number = randint(0,8) #picks random box
        indices = self.GetBoxi(box_number) #gets box indices
        self.movable_indices = list( set(indices) & set(self.nonfixed)) #gets movable box indices
        shuffle(self.movable_indices) #randomizes the order of filled in numbers
        i1 = self.movable_indices[0] #picks first 2 random indices
        i2 = self.movable_indices[1]
        
        Energy_old = self.GetEnergy() #finds energy
        self.SwapEntries(i1,i2) #swaps entries
        Energy_new = self.GetEnergy() #finds new energy
        DeltaE = Energy_old - Energy_new
        self.SwapEntries(i1,i2) #swaps entries back
        if Energy_new <= Energy_old:
            self.SwapEntries(i1,i2)
        elif np.random.random() <= np.exp(float(DeltaE/self.T)):
            self.SwapEntries(i1,i2)
        
        if (self.count % 1000) == 0: #Sweeps Puzzle to imporve performance and print periodic updates
            print "count:",self.count,"Energy:",Energy_new, "Temperature:", self.T
            if self.anneal == 'yes':
                self.T *= 0.99 #lowers temperature as part of cooling schedule. Lower value to cool faster
            self.energies.append(Energy_new)
            self.counts.append(self.count)
            
            
        if self.Energy == 0: #if the puzzle is solved
            print "Winner!!!! Solution:"
            print "final count:",self.count, "Temperature:", self.T
            print np.reshape(self.ReturnPuzzle(), (9, 9)) #print the list reshaped as a matrix
            self.energies.append(Energy_new) #adds final energy to the energy list
            self.counts.append(self.count) #adds final count to the count list
            self.win = True #sets win variable to true
            self.wincount = self.count #stores the winning count value
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

def SolvePuzzle(Puzzle,plot,anneal): #takes puzzle as argument. Also plot and anneal = 'yes' or 'no'
    Sudoku = SudokuMaker(anneal) #creates SudokuMaker Instance with anneal option
    Matrix = copy.copy(Puzzle) #makes sure the Solving puzzle isnt still linked to the original input
    Sudoku.MatrixAssign(Matrix)
    print "original puzzle: (0 implies empty slot)"
    Sudoku.PrintPuzzle()
    Sudoku.RandomiseZeros() #randomises zeros in each box from 1-9
    for i in range(50001): #runs iterations in range. 1 over to make sure final update is given
        Sudoku.Metropolis()
        if Sudoku.wincount != 0 or i == 50000:
            if plot == 'yes': #if you win
                if Sudoku.wincount != 0:
                    color1 = 'green'
                    color2 = 'blue'
                
                elif plot == 'yes': #keep losing colors
                    color1 = 'red'
                    color2 = 'pink'
                
                fig = plt.figure(0)
                red_patch = mpatches.Patch(color='red', label='Unsuccessful Solve')
                blue_patch = mpatches.Patch(color='green', label='Successful Solve')
                plt.legend(handles=[red_patch, blue_patch], prop={'size': 26})
                plt.plot(Sudoku.counts,Sudoku.energies,color = color1)
                plt.scatter(Sudoku.count,Sudoku.Energy,s=80, facecolors=color2, edgecolors=color1)
                plt.xlabel("iterations")
                plt.ylabel("Energy")
                plt.show()
                
            variableskip = Sudoku.wincount
            del Sudoku
            return variableskip  #exit function and return the count at which puzzle was solved        
    variableskip = Sudoku.wincount
    del Sudoku
    return variableskip

def EnergyPlot(T0,Puzzle):
    Sudoku = SudokuMaker('no',T0 = T0) #creates SudokuMaker Instance with anneal option
    Matrix = copy.copy(PuzzleStandard) #makes sure the Solving puzzle isnt still linked to the original input
    Sudoku.MatrixAssign(Matrix)
    print "original puzzle: (0 implies empty slot)"
    Sudoku.PrintPuzzle()
    Sudoku.RandomiseZeros() #randomises zeros in each box from 1-9
    for i in range(50001): #runs iterations in range. 1 over to make sure final update is given
        Sudoku.Metropolis()
        if Sudoku.wincount != 0 or i == 50000:
            variableskip = Sudoku.GetEnergy()
            del Sudoku
            return variableskip  #exit function and return the count at which puzzle was solved 
    

""" Solving Puzzle """

def RatioCalculate(Puzzle,plot,anneal,label):
    wins = [] #counts at which wins are achieved
    win_count = 0.0 #number of wins
    Puzzles = 5 #number of iterations per puzzle type
    for i in range(Puzzles):
        print i,"/1000" #loading bar
        finalcounter = SolvePuzzle(Puzzle,plot,anneal) #counter = final puzzle counter
        if finalcounter != 0: #if final counter is not 0
            win_count += 1 #add 1 win to win count
            wins.append(finalcounter)
    if wins != []:
        fig = plt.figure(1)
        plt.hist(wins,alpha = 0.5,bins = np.linspace(0,50001,15),histtype = 'barstacked',label = label)
        plt.xlabel("iterations")
        plt.ylabel("Puzzles Solved")
        plt.show()
    plt.legend(prop={'size':25})
    print "Win/Puzzle Ratio = ",win_count/Puzzles


""" Calling Solver """

### Use: RatioCalculate(Puzzle,plot,anneal,label)
### Puzzle is the called Sudoku puzzle to solve; PuzzleEasy, PuzzleStandard, PuzzleHard
### plot decides whether to plot energy profile; 'yes','no'
### anneal either sets initial temperature to either 0.5 (anneal case) or 0.000000000001 (almost 0): 'yes','no'
### label is the legend label shown in the energy plot

#RatioCalculate(PuzzleEasy,'yes','yes','Easy')
#RatioCalculate(PuzzleStandard,'yes','yes','Standard')
#RatioCalculate(PuzzleHard,'yes','yes','Hard')

T_list = np.linspace(0,4,75)

Energy_list = []
for i in T_list:
    Energies = []
    for j in range(40):
        Energies.append(EnergyPlot(i,PuzzleEasy))
    Energy_list.append(np.average(Energies))
plt.grid(True)
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.plot(T_list,Energy_list,color = 'green')
plt.scatter(T_list,Energy_list,color = 'green',label = 'Easy')
plt.legend(prop={'size':25}, loc = 'upper left')

Energy_list = []
for i in T_list:
    Energies = []
    for j in range(40):
        Energies.append(EnergyPlot(i,PuzzleStandard))
    Energy_list.append(np.average(Energies))
plt.grid(True)
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.plot(T_list,Energy_list,color = 'blue')
plt.scatter(T_list,Energy_list,color = 'blue',label = 'Standard')
plt.legend(prop={'size':25}, loc = 'upper left')

Energy_list = []
for i in T_list:
    Energies = []
    for j in range(40):
        Energies.append(EnergyPlot(i,PuzzleHard))
    Energy_list.append(np.average(Energies))
plt.grid(True)
plt.xlabel("Temperature")
plt.ylabel("Energy")
plt.plot(T_list,Energy_list,color = 'Red')
plt.scatter(T_list,Energy_list,color = 'Red',label = 'Hard')
plt.legend(prop={'size':25}, loc = 'upper left')