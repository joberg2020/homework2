#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:46:05 2023

@author: jo223cy
@author: Eliassj
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Callable, Union


class Interval:
    """
    The Interval class represents a range of real numbers defined '
    by a lower and upper bound.

    Attributes:
        _lowest (int, float)
            The lowest value of the interval.
        _highest (int, float)
            The highest value of the interval.
    """

    def __init__(self, lowest: Union[int, float],
                 highest: Union[int, float] = None):
        """
        The constructor for the Interval class.

        Parameters:
            lowest (int, float): The lowest value of the interval.
            highest (int, float): The highest value of the interval.
        """
        if highest is None:
            highest = lowest
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
        """
        Overloads the right subtraction method.

        Parameters
        ----------
        other : (int, float, Interval):
            The left side of the subtraction.

        Returns
        -------
        Interval
            The resulting interval.

        """
        if not isinstance(other, Interval):
            other = Interval(other)
        return other - self

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
        ValueError
            If result is an Interval that is infinitely large.
        ZeroDivisionError
            If denominator is zero or has zero in its interval.

        Returns
        -------
        Interval
            A new Interval that represents the interval of the division.
        """
        result = None
        sh = self._highest
        sl = self._lowest
        # Check if other is numeric then check div by zero
        if isinstance(other, (int, float)):
            if other != 0:
                result = Interval(sl / other, sh / other)
            else:
                raise ZeroDivisionError("Can't divide by zero.")
        elif isinstance(other, Interval):
            if 0 not in other:
                oh = other._highest
                ol = other._lowest
                L = [sh / oh, sh / ol, sl / oh, sl / ol]
                result = Interval(min(L), max(L))
            else:
                raise ZeroDivisionError("Can't divide by zero.")
        else:
            raise TypeError("Can't divide non-numeric")

        # Check for infinity
        if float('-inf') in result or float('inf') in result:
            raise ValueError("The resulting interval is infinitely large.")

        return result

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
        Returns a string representation of the Interval object.

        Returns
        -------
        str
            A string representation of the Interval in the form
            "[lowest, highest]".
        """
        return f"[{self._lowest}, {self._highest}]"

    def _validate_is_number(self, value):
        """
        Helper function to validate input for Interval.

        Parameters
        ----------
        value : any
            The value to validate.

        Raises
        ------
        TypeError
            If value is of other type than int or float.

        Returns
        -------
        None.

        """
        if not isinstance(value, (int, float)):
            raise TypeError('Only int and float are supported.')

    def __contains__(self, value: Union[int, float]) -> bool:
        """
        Overloads the contains function for Ithe nterval class.

        Parameters
        ----------
        value : Union[int, float]
            Accepts int or float.

        Returns
        -------
        bool
            True if the number is captured by the current Interval, False
            otherwise.

        """
        self._validate_is_number(value)
        return value >= self._lowest and value <= self._highest

    def __neg__(self):
        """
        Overloafs the negative operator for class Interval.
        Returns a negative of the current interval.

        Returns
        -------
        Interval
            The negative counterpart of the current interval.

        """
        return Interval(-self._highest, -self._lowest)

    def __pow__(self, exponent: int):
        """
        Parameters
        ----------
        exponent : int
            The exponent.

        Raises
        ------
        TypeError
            If exponent is anything else than an integer, a
            TypeError will be thrown.

        Returns
        -------
        Interval
            The resulting Interval.

        """
        if not isinstance(exponent, int):
            raise TypeError("Only integers allowed as exponents.")
        if exponent % 2 != 0:
            return Interval(self._lowest**exponent, self._highest**exponent)
        # exponent is even - three cases:
        else:
            if self._lowest >= 0:
                return Interval(self._lowest**exponent,
                                self._highest**exponent)
            elif self._highest < 0:
                return Interval(self._highest**exponent,
                                self._lowest**exponent)
            else:
                return Interval(0, max(self._lowest**exponent,
                                       self._highest**exponent))

    @staticmethod
    def plot_bounds(polynomial: Callable, x_intervals: list, title: str):
        """
        Plot the lower and upper bounds of a given polynomial over a list of
        intervals.

        The function computes the polynomial for each interval in x_intervals
        and then plots the lower and upper bounds of the results. The plot
        is given a title specified by the user.

        Parameters
        ----------
        polynomial : Callable
            The polynomial function to be evaluated. This function should
            accept an Interval object and return an Interval object
            representing the lower and upper bounds of the polynomial
            over that interval.
.
        x_intervals : list
            A list of Interval objects representing the intervals over which
            the polynomial should be evaluated.

        title : str
            The title of the plot.

        Returns
        -------
        None.

        """
        try:
            x_low = [elem._lowest for elem in x_intervals]

            y_intervals = [polynomial(interv) for interv in x_intervals]
            y_low = []
            y_high = []
            for idx, elem in enumerate(y_intervals):
                y_low.append(elem._lowest)
                y_high.append(elem._highest)
            plt.plot(x_low, y_low)
            plt.plot(x_low, y_high)
            plt.title(title)
            plt.xlabel("x")
            plt.ylabel("p(I)")
            plt.show()
        except Exception as e:
            print('Exception occured', e)


# Code for evaluating task 10
def p(iv):
    return 3 * iv**3 - 2 * iv**2 - 5 * iv - 1


def get_intervals():
    xl = np.linspace(0., 1, 1000)
    xu = np.linspace(0., 1, 1000) + 0.5
    return [Interval(xl[(i)], xu[i]) for i in range(len(xl))]


Interval.plot_bounds(p, get_intervals(), "p(I) = 3 * I³ - 2 * I² - 5 * I - 1;"
                     " I = Interval(x, x + 0.5)")
