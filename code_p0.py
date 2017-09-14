import glob
import numpy as np
import matplotlib.pyplot as plt





def phase(mjd, P):  
    return (mjd/P)%1

mjd1,m1= np.genfromtxt('star2.txt',usecols= (0,1), unpack= True)
P1=float(1/2.057351)
plt.figure(figsize=(7,7))
plt.errorbar(phase(mjd1, P1),m1, fmt='o', color='gray')
plt.errorbar(phase(mjd1, P1)+1,m1, fmt='o', color='gray')
plt.xlabel('Fase')
plt.ylabel('Magnitud Aparente')
plt.gca().invert_yaxis()
plt.show()


def phase1(mjd1, P1):  
    return (mjd1/P1)%1

mjd1, m1= np.genfromtxt('star1.txt',usecols= (0,1), unpack= True)
P1=float(1/1.154652925)
plt.figure(figsize=(7,7))
plt.errorbar(phase1(mjd1, P1), m1, fmt='o', color='blue')
plt.errorbar(phase1(mjd1, P1)+1, m1, fmt='o', color='blue')
plt.xlabel('Fase')
plt.ylabel('Magnitud Aparente')
plt.gca().invert_yaxis()
plt.show()
