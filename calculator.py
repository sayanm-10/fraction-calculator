#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.2.0"
__license__ = "MIT"

import unittest
from fraction import Fraction, FractionTest

validOperators =  ['+', '-', '*', '/', '==', '!=', '<', '<=', '>', '>=']

def main():
    ''' Main entry point for the app '''

    fraction1 = createFraction('Fraction 1')
    operator = getOperator()
    fraction2 = createFraction('Fraction 2')
    
    print("\nFirst fraction is", fraction1)
    print("\nSecond fraction is", fraction2)
    printResult(fraction1, fraction2, operator)

def createFraction(fracName):
    ''' Returns a valid fraction instance.
        Takes a string to denote as label for the console message. '''

    numerator = getNumber('\nNumerator for {} :'.format(fracName))
    
    while True:
        denominator = getNumber('\nDenominator for {} :'.format(fracName))
        try:
            return Fraction(numerator, denominator)
        except ValueError as e:
            print(e)

def printResult(frac1, frac2, op):
    ''' returns and instance of the Fraction class after computing given operation '''

    if op == '+':
        print('\n{} + {} = {}'.format(frac1, frac2, frac1 + frac2))
    elif op == '-':
        print('\n{} - {} = {}'.format(frac1, frac2, frac1 - frac2))
    elif op == '*':
        print('\n{} * {} = {}'.format(frac1, frac2, frac1 * frac2))
    elif op == '/':
        print('\n{} / {} = {}'.format(frac1, frac2, frac1 / frac2))
    elif op == '==':
        print('\n{} == {} = {}'.format(frac1, frac2, frac1 == frac2))
    elif op == '!=':
        print('\n{} != {} = {}'.format(frac1, frac2, frac1 != frac2))
    elif op == '<':
        print('\n{} < {} = {}'.format(frac1, frac2, frac1 < frac2))
    elif op == '<=':
        print('\n{} <= {} = {}'.format(frac1, frac2, frac1 <= frac2))
    elif op == '>':
        print('\n{} > {} = {}'.format(frac1, frac2, frac1 > frac2))
    elif op == '>=':
        print('\n{} >= {} = {}'.format(frac1, frac2, frac1 >= frac2))

def getOperator():
    ''' returns the operator chosen by the user '''

    while True:
        operator = input("\nChoose one operator: {} ".format(validOperators))
        if operator in validOperators:
            return operator
        else:
            print("\nInvalid operator!")

def getNumber(message):
    ''' Function accepts a string message to show on the console
        and returns an integer value or shows ValueError exception '''

    while True:
        number = input(message)
        try:
            return int(number) # float?
        except ValueError:
            print('\n{} is not an integer! Please enter an integer value.'.format(number))

if __name__ == "__main__":
    """ This is executed when run from the command line """
    
    unittest.main(exit=False, verbosity=2)
    main()