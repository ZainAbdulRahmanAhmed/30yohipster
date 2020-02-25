# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 16:48:57 2020

@author: zain AR ahmed
"""

import math

class Circle(object):
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        a = round(2 * math.pi * self.radius, 3)
        print(f'The radius of the circle is {a}.')

print('''
This program lets you find the area of a circle based on its radius and rounds it to 3 decimal places.
Type "exit" to end the program.''')

while True:
    r = (input('> '))
    if not r.isalpha():
        circle = Circle(float(r))
        circle.area()
    if r.isalpha():
        r = r.lower()
        if r == 'exit':
            print('Goodbye.')
            break
        else:
            print('Invalid input. Try again.')