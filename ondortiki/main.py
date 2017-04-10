#Bolum:14 Ornek:2
#(14.2) En Hizli Artis Yolunun Hesaplanmasinda Gradyenin Kullanilmasi
from sympy import *
import math
x=Symbol('x')
y=Symbol('y')
xi=2                #x degeri
yi=2                #y degeri
denklem=x*y**2      #denklem
def deltaf(denklem,xi,yi):
    xturev=denklem.diff(x).subs(x,xi).subs(y,yi)
    yturev=denklem.diff(y).subs(x,xi).subs(y,yi)
    return xturev,yturev,math.sqrt(xturev*xturev+yturev*yturev),math.degrees(math.atan(yturev/xturev))
#print "Delta f(x,y): "+deltaf(denklem,xi,yi).__str__()
#print math.degrees(math.atan(8/4))
print "Aci (derece): "+deltaf(denklem,xi,yi)[3].__str__()+" \nYukselis miktari (birim): "+deltaf(denklem,xi,yi)[2].__str__()