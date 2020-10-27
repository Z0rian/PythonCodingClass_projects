# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 10:22:25 2020

@author: zorian
"""

class Fraction():
    
    def __init__(self, num, den):
        self.num = num
        self.den = den
        
        
    def __str__(self):
        return f'{self.num}/{self.den}'
    
    def __add__ (self, frac2):
        new_num = self.num * frac2.den + frac2.num *self.den
        new_den = self.den * frac2.den
        new_frac = Fraction(new_num, new_den)
        return new_frac
    
    def gcd(self):
        a = self.num
        b = self.den
        if a == 0:
            return a
        return self.gcd(b, a % b)
    
class Mixed(Fraction):
        
        def __init__(self, whole, num, den):
            self.whole = whole
            self.num = num
            self.den = den
            
        def __str__(self):
            return f'{self.whole} {self.num}/{self.den}'
        
        def improper(self):
            new_num = self.den * self.whole + self.num
            new_den = self.den
            return Fraction(new_num, new_den)
        
        def __add__(self, frac2):
            return self.improper() + frac2.improper()
        
        
f1 = Mixed(3, 1, 2) 
print (f1)
print (f1.improper())
print(f1 + f1)