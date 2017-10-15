import math
from math import sin, cos, log
c = int(input('Enter c = 1 or 2 or 3:'))
if c == 1:
    a = float(input('Enter a:'))
    x = float(input('Enter x:'))
    G = 5 * (-2 * a ** 2 + a * x + 3 * x ** 2) / (-10 * a ** 2 + 11 * a * x + 3 * x ** 2)
    print ('a = {}, x = {}, Result: {}'.format(a, x, G))

if c == 2:
    a = float(input('Enter a:'))
    x = float(input('Enter x:'))
    F = sin(10 * a ** 2 - 7 * a * x + x ** 2)
    print ('a = {}, x = {}, Result: {}'.format(a, x, F))

if c == 3:
    a = float(input('Enter a:'))
    x = float(input('Enter x:'))
    Y = sin(1) / cos(45 * a ** 2 - 79 * a * x + 30 *x ** 2)
    print ('a = {}, x = {}, Result: {}'.format(a, x, Y))
if (c != 1) and (c != 2) and (c != 3):
    print ('Error')
