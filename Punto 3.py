import numpy as np

VY = np.array([-63.87,-63.78,-60.37,-80.68,-32.17,-27.61,-34.49,-82.60,-10.20,-43.90,-79.89,-6.78,-80.31,-85.57,-20.88,-13.79,-36.93,-14.17,-20.76,-5.28,-34.62,-12.52,-46.30,-27.30,-75.35,-14.77,-85.87,-32.44,-76.05,-79.18,-86.43,-12.57,-42.85,-60.19,-44.04,-83.98,-11.13,-85.33,-20.21,-76.10])

VX = np.array([
     [9.52,10.90,9.61,11.51,5.48,3.83,4.37,13.17,4.07,5.42,12.12,7.31,14.88,12.92,5.97,11.22,7.28,6.68,6.69,4.10,9.27,5.05,10.27,5.38,10.52,5.17,14.94,6.78,8.52,13.10,13.80,4.92,7.79,7.52,9.16,12.95,5.17,14.59,4.62,14.44],
     [41.82,30.19,33.69,29.20,43.08,47.60,47.12,28.40,42.40,32.88,29.06,30.18,26.98,27.92,44.99,27.91,31.87,34.14,34.40,39.44,29.20,43.43,29.53,39.81,30.12,44.93,27.30,36.69,31.10,28.51,27.91,42.86,36.94,36.53,28.31,25.40,46.29,27.81,42.59,26.46]
])

n = len(VX[0])
VX = np.insert(VX, 0, np.ones(n), axis=0)
k =len(VX)
ypro=(sum(VY))/n
prom=[]
g = np.zeros(k)
A = np.zeros((k, k))


for i in range(0, k):
    for j in range(0, k):
        A[i, j] = sum(VX[i, :]*VX[j, :])
    g[i] = sum(VX[i, :]*VY)
print('A =','\n',A)
print('invA =','\n',np.linalg.inv(A))
print('g =','\n',g)
b = np.dot(np.linalg.inv(A), g)


VX = np.delete(VX, 0, axis=0)

e2 = np.zeros(n)

# no borrar xD

aux = 0
bx= b[1:k]
b0 = b[0]

for i in range (0,n):
    for j in range (0, k-1):
        aux = aux - (bx[j]*VX[j,i])
    e2[i] = (VY[i]-b0 + aux)**2
    aux=0


for i in range (0,k):
    print("b%d = %f." %(i,b[i]))

for i in range (0,n):
    st=(VY[i]-ypro)**2
    prom.append(st)


print ('y(35,250)=',b[0]+(b[1]*35)+(b[2]*250))
print("\nSr = ",sum(e2))
print('St =',sum (prom))
print('Sy^2 =',round ((sum(prom)/(n-1)),4))#varianza
print('Sy =',round ((sum(prom)/(n-1))**(1/2),4))#desviación estandar
print('Sy/x =',round (((sum(e2)/(n-((k-1)+1))))**(1/2),4))#error estandar de estimación
print('r^2 =',round ((sum(prom)-sum(e2))/sum(prom),4))#coeficiente de determinación
print('r =',round (((sum(prom)-sum(e2))/sum(prom))**(1/2),4))#coeficiente de relación o de correlación


