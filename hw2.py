#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:46:05 2023

@author: jo223cy
"""

import numpy as np
import matplotlib.pyplot as plt


class interval:

    def __init__(self, lowest: float, highest: float):
        self._lowest = lowest
        self._highest = highest
        
    def __add__(self, other): # Add method
        # Check if other is numeric
        if isinstance(other, (int, float, interval)) == False:
            raise TypeError("Can't add non-numeric")
        sh = self._highest
        sl = self._lowest
        if isinstance(other, (int, float)):
            return interval(sl + other, sh + other)
        elif isinstance(other, interval):
            oh = other._highest
            ol = other._lowest
            return interval(sl + ol, sh + oh)
        
    def __radd__(self, other): # Funkar inte, varför?
        return self + other
    
    def __sub__(self, other): # Subtract method
        # Check if other is numeric
        if isinstance(other, (int, float, interval)) == False:
            raise TypeError("Can't subtract non-numeric")
        sh = self._highest
        sl = self._lowest
        if isinstance(other, (int, float)):
            return interval(sl - other, sh - other)
        elif isinstance(other, interval):
            oh = other._highest
            ol = other._lowest
            return interval(sl - oh, sh - ol)
    
    def __rsub__(self, other):
        return self - other
    
    def __mul__