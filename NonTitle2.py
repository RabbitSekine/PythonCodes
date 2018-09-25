# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:12:42 2018

@author: asekine
"""


class Triangle:
    def __init__(self,b,h):
        self.base=b
        self.height=h
        
    def area(self):
        return(self.base*self.height/2)
        
        
t1=Triangle(5,5)
print(t1.area())