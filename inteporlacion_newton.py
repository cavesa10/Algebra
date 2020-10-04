import numpy as np
from sympy import Symbol, log

x = Symbol('x')
fx = log(x) # Definir función
z = 2 # El valor que desea aproximar
fz = fx.subs(x, z).evalf()

VX = np.array ([1,4,6]) # Vector X
n = len(VX) 

VY = np.ones(n)

for i in range(0,n):
   VY[i] = fx.subs(x, VX[i]).evalf()

DifX= np.zeros((n,n))
DifX[0:1] = VX

Dif= np.zeros((n,n))
Dif[0:1] = VY

for i in range(1,n):
  for j in range(0, n-1):
    if (j < n-i):
      DifX[i,j] = (DifX[0,i+j]-DifX[0,j])

for i in range(1,n):
  for j in range(0, n-1):
    if (j < n-i):
      Dif[i,j] = (Dif[i-1,j+1]-Dif[i-1,j])/(DifX[i,j])

b= Dif[:,0]

Tn = 1
fn = b[0]

print(fn)
for i in range (1,n):
  Tn = Tn * (z-VX[i-1])
  fn = fn + b[i]*Tn
  print("Aproximación", i, " = ",fn)

Et = (fz-fn)/fz
Ev = fz - fn


print("Con un polinomio de grado %d, la aproximación para x = %f es %f" %(n,z,fn))