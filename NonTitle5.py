# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 19:04:09 2018

@author: asekine
"""



class Square:
    square_list=[]
    
    def __init__(self,s):
        self.side=s
        
        self.square_list.append(self)
        
    def __repr__(self):
      
        return "{} by {} by {} by {}".format(self.side,self.side,self.side,
                self.side)
        
s1=Square(10)
s2=Square(70)
print(s2)

        