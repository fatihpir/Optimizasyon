from sympy import *
import math

x = Symbol('x')
y = Symbol('y')

xi = 1  # x degeri
yi = 1  # y degeri

denklem = 2 * x ** 3 * y ** 2 - 6 * x * y + x ** 2 + 4 * y
print denklem

print "Denklem:" + denklem.diff(x).subs(x, xi).subs(y, yi).__str__() + "cos T + " + denklem.diff(y).subs(x, xi).subs(y,yi).__str__() + "sin T"
