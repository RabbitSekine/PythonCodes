# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:52:00 2018

@author: asekine
"""


class Rider:
    def __init__(self,name):
        self.name=name

class Hose:
    def __init__(self,name,bleed,rider):
        self.name=name
        self.bleed=bleed
        self.rider=rider
        

        
jockey1=Rider("Take")
sarab1=Hose("Kitasan","Sarabled",jockey1)
print(sarab1.name)
print(sarab1.rider.name)