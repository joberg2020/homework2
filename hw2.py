#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:46:05 2023

@author: jo223cy
@author: Eliassj
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Union


class Interval:
    """
    The Interval class represents a range of real numbers defined by a lower and upper bound.

    Attributes:
        _lowest (float)
            The lowest value of the interval.
        _highest (float)
            The highest value of the interval.
    """

    def __init__(self, lowest: Union[int, float], highest: Union[int, float]):
        """
        The constructor for the Interval class.

        Parameters:
            lowest (int, float): The lowest value of the interval.
            highest (int, float): The highest value of the interval.
        """
        if not (isinstance(lowest, (int, float)) and
                isinstance(highest, (int, float))):
            raise TypeError("Only int and float are supported.")
        self._lowest = lowest
        self._highest = highest

    def __add__(self, other):
        """
       Overloads the addition operator for the Interval class.

       Parameters
       ----------
           other (Interval, int, float): The Interval (or number) to add.

       Returns
       -------
           Interval
               A new Interval that represents the interval of the sum.
       """
        # Check if other is numeric
        if not isinstance(other, (int, float, Interval)):
            raise TypeError("Can't add non-numeric")
        sh = self._highest
        sl = self._lowest
        if isinstance(other, (int, float)):
            return Interval(sl + other, sh + other)
        elif isinstance(other, Interval):
            oh = other._highest
            ol = other._lowest
            return Interval(sl + ol, sh + oh)

    def __radd__(self, other):
        """
        Overloads the addition operator for right addition.

        Parameters
        ----------
            other (Interval, int, float): The Interval (or number) to add.

        Raises
        ------
        TypeError
            If other is not of type int, float or Interval.
        Returns
        -------
            Interval: A new Interval that represents the interval of the sum.

        """
        return self + other

    def __sub__(self, other):
        """
        Overloads the subtraction operator (-) for the Interval class.

        This method subtracts a number (int, float) or another Interval
        object from this Interval. If `other` is a number,it's subtracted
        from both the lower and upper bounds. If `other` is an Interval,
        the highest bound of `other` is subtracted from the lowest bound
        of `self`, and the lowest bound of `other` is subtracted from the
        highest bound of `self` to form the new Interval.

       Parameters
       ----------
       other (Interval, int, float):
           The Interval (or number) to be subtracted from this Interval.

       Raises
       ------
       TypeError
           If `other` is not of type int, float, or Interval.

       Returns
       -------
       Interval
           A new Interval that represents the range of possible
           values after the subtraction.

       """
        # Check if other is numeric
        if not isinstance(other, (int, float, Interval)):
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
        """
        Overloads the multiplication operator for the Interval class.

        Parameters
        ----------
        other (Interval, int, float):
            The Interval (or number) to multiply.

        Raises
        ------
        TypeError
            If other is not of type int, float or Interval.

        Returns
        -------
        Interval
            A new Interval that represents the interval of the product.
        """
        # Check if other is numeric
        if not isinstance(other, (int, float, Interval)):
            raise TypeError("Can't multiply non-numeric")
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
        """
        Overloads the right-hand-side multiplication operator for the
        Interval class.

        Parameters
        ----------
        other (int, float):
            The number (or Interval) to multiply the Interval with.

        Returns
        -------
        Interval
            A new Interval that represents the interval of the product.
        """
        return self * other

    def __truediv__(self, other):
        """
        Overloads the division operator for the Interval class.

        Parameters
        ----------
        other (Interval, int, float):
            The Interval (or number) to divide.

        Raises
        ------
        TypeError
            If other is not of type int, float or Interval.

        Returns
        -------
        Interval
            A new Interval that represents the interval of the division.
        """
        # Check if other is numeric
        if not isinstance(other, (int, float, Interval)):
            raise TypeError("Can't divide non-numeric")
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
        """
        Overloads the right-hand-side division operator for the Interval class.

        Parameters
        ----------
        other ´(int, float):
            The number to divide by the Interval.

        Returns
        -------
        Interval
            A new Interval that represents the interval of the division.
        """
        return Interval(other / self._highest, other / self._lowest)

    def __repr__(self):
        """
        Returns a formal string representation of the Interval object.

        This method is used by built-in functions and modules like repr(),
        or when a string conversion of an object is required. It should
        represent an unambiguous string that can be used to recreate the
        object when fed to the eval() function.

        Returns
        -------
        str
            A string representation of the Interval in the form "Interval[lowest, highest]".
        """
        return f"Interval[{self._lowest}, {self._highest}]"

    def __str__(self):
        """
        Returns a string representation of the Interval object.

        Returns
        str
            A string representation of the Interval in the form
            "[lowest, highest]".

        """
        return f"[{self._lowest}, {self._highest}]"


a = Interval(23, 67)
b = Interval(67, 120)