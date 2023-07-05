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
