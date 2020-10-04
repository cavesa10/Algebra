from sympy import Symbol, log
import math

x = Symbol('x')
fx= log(x**2) + 2

xinf = float(input('ingrese el extremo inferior Xinf='))  # 12
xsup = float(input('ingrese el extremo superior Xsup='))  # 16
Es = float(input('Ingrese la tolerancia porcentual, Es= '))  # 0.5
raiz = float(input('ingrese la raiz a aproximar ='))  # 14.8011
fxinf = fx.subs(x, xinf)
print(fxinf)


i = 0
xr = 1
print('n\t Xinf\t Xsup\t Xr\t Et\t Ea')

while True:
    i = i+1
    xr_ant = xr
    xr = (xinf + xsup)/2
    fxr = fx.subs(x, xr)
    signo = fxr*fxinf
    Ea = abs((xr-xr_ant)/xr)*100
    Et = abs((raiz-xr)/raiz)*100
    if i == 1:
        print(i, '\t', xinf, '\t', xsup, '\t', xr,
              '\t', round(Et, 4), '%\t', "----")
    else:
        print(i, '\t', xinf, '\t', xsup, '\t', xr, '\t',
              round(Et, 4), '%\t', round(Ea, 4), '%')
    if (signo < 0):
        xsup = xr
    elif signo > 0:
        xinf = xr

    if signo == 0 or Ea <= Es:
        break

# if (k == 3):
#     for i in range(0, n):
#         e2[i] = (VY[i]-b[0]-(b[1]*VX[0, i])-(VX[1, i]*b[2]))**2
#     print(e2)
#     print(sum(e2))
# elif (k == 4):
#     for i in range(0, n):
#         e2[i] = (VY[i]-b[0]-(b[1]*VX[0, i])-(VX[1, i]*b[2])-(VX[2, i]*b[3]))**2
#     print(e2)
#     print(sum(e2))
# elif (k == 5):
#     for i in range(0, n):
#         e2[i] = (VY[i]-b[0]-(b[1]*VX[0, i])-(VX[1, i]*b[2])-(VX[2, i]*b[3])-(VX[3, i]*b[4]))**2
#     print(e2)
#     print(sum(e2))
# elif (k == 6):
#     for i in range(0, n):
#         e2[i] = (VY[i]-b[0]-(b[1]*VX[0, i])-(VX[1, i]*b[2])-(VX[2, i]*b[3])-(VX[3, i]*b[4])-(VX[4, i]*b[5]))**2
#     print(e2)
#     print(sum(e2))