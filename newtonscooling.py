# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 13:02:40 2017

@author: Cormac
"""

import numpy as np

### Module using Newtons Law of Cooling to Simulate Cooling
### Initialised with starting temperate T_0, Surroundings
### temperature T_s and a cooling rate.
###
###
###

class CoolingFunction:
        def __init__(self,T_0,T_s,rate): #n = size of matrix
            self.T_0 = T_0
            self.T_s = T_s
            self.rate = rate            
            
        def Analytic(self,t): # defines function that takes time in analytic function
            return float(self.T_s-(self.T_s-self.T_0)*np.exp(-self.rate*t)) # returns arguemnt through function

