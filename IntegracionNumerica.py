import numpy as np
from sympy import Symbol, log, integrate

M = np.array([
    [-8,-8,-6,4],
    [-4,-3,1,7],
    [-2,-1,4,10]
  ]
)
dx = 4
dy = 2

a = 0
b = 12

c = 0
d = 4

col = len(M[0])
f = len(M[0:col])

Tn = np.zeros(col)

opcion = input('Ingreser 1 si x, 2 si es y: ')

if (opcion == '1'):
  for i in range(0, col):
    numbers = np.array(np.flip(M[:,i]))
    sum = numbers[0]
    for  j in range(1,f-1):
      sum  = sum + 2*numbers[j]
    Tn[i]= (dy/2) * (sum + numbers[f-1])

  print(Tn)

  sum = Tn[0]
  for  j in range(1,f-1):
    sum  = sum + 2*Tn[j]
  integral= (dx/2) * (sum + Tn[col-1])

  fprom = integral/((d-c)*(b-a))

  print(integral)
  print(fprom)

elif (opcion == '2'):
  for i in range(0, col):
    numbers = np.array(np.flip(M[:,i]))
    sum = numbers[0]
  for  j in range(1,f-1):
    if(i%2 ==0):
      sum = sum + 2*numbers[j]
    else:
      sum = sum + 4*numbers[j]
  Tn[i]= (dy/3) * (sum + numbers[f-1])

else:
  input("Opcion invalida")



