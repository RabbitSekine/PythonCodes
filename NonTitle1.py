# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:12:42 2018

@author: asekine
"""

import math

class Circle:
    def __init__(self,r):
        self.radius=r
        
    def area(self):
        return(math.pi*self.radius**2)
        
        
c1=Circle(5)
print(c1.area())