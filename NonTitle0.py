# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 14:05:42 2018

@author: asekine
"""

class Apple:
    def __init__(self,w,c,t,s):
        self.weight=w
        self.color=c
        self.taste=t
        self.smell=s
        
ap1=Apple(34,"red","sour","sweet")
print(ap1.smell)