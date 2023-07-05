#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:46:05 2023

@author: jo223cy
"""

import numpy as np
import matplotlib.pyplot as plt


class Interval:

    def __init__(self, lowest: float, highest: float):
        self._lowest = lowest
        self._highest = highest
        
    def __add__(self, other): # Add method
        # Check if other is numeric
        if isinstance(other, (int, float, Interval)) == False:
            raise TypeError("Can't add non-numeric")
        sh = self._highest
        sl = self._lowest
        if isinstance(other, (int, float)):
            return Interval(sl + other, sh + other)
        elif isinstance(other, Interval):
            oh = other._highest
            ol = other._lowest
            return Interval(sl + ol, sh + oh)
        
    def __radd__(self, other): # Funkar inte, varför?
        return self + other
    
    def __sub__(self, other): # Subtract method
        # Check if other is numeric
        if isinstance(other, (int, float, Interval)) == False:
            raise TypeError("Can't subtract non-numeric")
        sh = self._highest
        sl = self._lowest
        if isinstance(other, (int, float)):
            return Interval(sl - other, sh - other)
        elif isinstance(other, Interval):
            oh = other._highest
            ol = other._lowest
            return Interval(sl - oh, sh - ol)
    
    def __rsub__(self, other):
        return self - other
    
    def __mul__(self, other):
        # Check if other is numeric
        if isinstance(other, (int, float, Interval)) == False:
            raise TypeError("Can't subtract non-numeric")
        sh = self._highest
        sl = self._lowest
        if isinstance(other, (int, float)):
            return Interval(sl * other, sh * other)
        elif isinstance(other, Interval):
            oh = other._highest
            ol = other._lowest
            L = [sh * oh, sh * ol, sl * oh, sl * ol]
            return Interval(min(L), max(L))
    
    def __rmul__(self, other):
        return self * other
    
    def __truediv__(self, other):
        # Check if other is numeric
        if isinstance(other, (int, float, Interval)) == False:
            raise TypeError("Can't subtract non-numeric")
        sh = self._highest
        sl = self._lowest
        if isinstance(other, (int, float)):
            return Interval(sl / other, sh / other)
        elif isinstance(other, Interval):
            oh = other._highest
            ol = other._lowest
            L = [sh / oh, sh / ol, sl / oh, sl / ol]
            return Interval(min(L), max(L))
        
    def __rtruediv__(self, other):
        return Interval(other / self._highest, other / self._lowest)
    
    def __repr__(self):
        return f"[{self._lowest}, {self._highest}]"
        
a = Interval(23, 67)
b = Interval(67, 120)