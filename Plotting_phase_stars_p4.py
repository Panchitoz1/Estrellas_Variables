# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:26:05 2017

@author: ffcarrasco
"""

import numpy as np
import matplotlib.pyplot as plt

def phase(mjd, P):  
    return (mjd/P)%1

#Parameters
mjd1, flux1, other1= np.genfromtxt('s1.txt',usecols= (0,1,2), unpack= True)
P1=float(1.38177359**(-1))
#P1=float(0.010335**(-1))
P1 = float('%.6f'%(P1))
A1 = 0.256766344 #mag

mjd2, flux2, other2= np.genfromtxt('s2.txt',usecols= (0,1,2), unpack= True)
P2=float(2.75008883**(-1))
P2 = float('%.6f'%(P2))
A2 = 0.427443961 #mag

print P1
print P2
### Plotting

#For star1.txt
plt.title('Flux vs. days for s1.txt')
plt.ylabel(r'Flux ($erg \cdot cm^{-2} \cdot s^{-1}$)')
plt.xlabel('JD')
plt.scatter(mjd1, flux1, s=0.3, color = 'red')
plt.savefig('s1txt_simple_plot.png', format = 'png')
plt.close()
#plt.figure(figsize=(7,7))

plt.title(r'Flux vs. Phase for s1.txt')
plt.scatter(phase(mjd1, P1),flux1, s = 0.3, color='red')
plt.xlabel('Phase')
plt.ylabel(r'Flux ($erg \cdot cm^{-2} \cdot s^{-1}$)')
plt.gca().invert_yaxis()
plt.savefig('s1txt_phase_plot.png', format = 'png')
plt.close()

#For star2.txt
plt.title('Flux vs. JD for s2.txt')
plt.ylabel(r'Flux ($erg \cdot cm^{-2} \cdot s^{-1}$)')
plt.xlabel('JD')
plt.scatter(mjd2, flux2, s= 0.3, color = 'black')
plt.savefig('s2txt_simple_plot.png', format = 'png')
plt.close()
#plt.figure(figsize=(7,7))

plt.title(r'Flux vs. Phase for s2.txt')
plt.scatter(phase(mjd2, P2),flux2, s = 0.3, color='black')
plt.xlabel('Phase')
plt.ylabel(r'Flux ($erg \cdot cm^{-2} \cdot s^{-1}$)')
plt.savefig('s2txt_phase_plot.png', format = 'png')
plt.show()
plt.close()
