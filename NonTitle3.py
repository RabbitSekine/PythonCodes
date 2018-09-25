# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:13:32 2018

@author: asekine
"""

class Shape:
    def what_am_i(self):
        print("I am a shape")
        
class Rectangle(Shape):
    def __init__(self,w,h):
        self.width=w
        self.height=h
   
    def calculate_perimeter(self):
        return self.width*2+self.height*2
        
class Square(Shape):
    def __init__(self,s):
        self.side=s
        
    def calculate_perimeter(self):
        return self.side*4
    
    def change_size(self,c):
        self.side += c
        
rec=Rectangle(10,30)
print(rec.calculate_perimeter())

sq=Square(10)
print(sq.calculate_perimeter())

sq.change_size(-8)
print(sq.calculate_perimeter())

sq.what_am_i()
rec.what_am_i()