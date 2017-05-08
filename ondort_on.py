from sympy import *
import math
x=Symbol('x')
y=Symbol('y')

xi=4    #x degeri
yi=2    #y degeri

denklem=5*x**2*y-8*y**2-7*x**2
#print denklem

print "Denklem:"+denklem.diff(x).subs(x,xi).subs(y,yi).__str__()+"cos T + " +denklem.diff(y).subs(x,xi).subs(y,yi).__str__() +"sin T"
