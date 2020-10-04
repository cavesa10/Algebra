import numpy as np
from sympy import Symbol, log, integrate

valorv =1.640533
#log(2)
a=0
b=0.8
n=5
x = Symbol('x')
fx =0.2+(25*x)-(200*(x**2))+(675*(x**3))-(900*(x**4))+(400*(x**5))
#1/x # Definir funció se cambia
delta = (b-a)/n #delta x en el libro lo llaman h
suma= fx.subs(x,a)

for i in range(1,n):
    xi = a + (i*delta)
    suma = suma + (2*(fx.subs(x,xi)))

suma = suma + fx.subs(x,b)
AT = (delta*suma)/2

EV= valorv - AT
Et=((valorv - AT)*100)/valorv
derivada2= fx.diff(x,2)
integral= integrate(derivada2,(x,a,b))
fprom=integral/(b-a)
Ea= -(((b-a)**3)/(12*n**2))*fprom
print("la aproximación con %d trapecios, es: %f"%(n,AT))
print('el error verdader0 es: %.8f'%(EV))
#print('f´´=',round(fprom,4))
print('Ea=',round(Ea,4))
print('Et=',round(Et,4),'%')


