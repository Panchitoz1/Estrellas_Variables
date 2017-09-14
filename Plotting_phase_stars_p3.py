# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:31:02 2017

@author: ffcarrasco
"""

import numpy as np
import matplotlib.pyplot as plt

def phase(mjd, P):  
    return (mjd/P)%1

#Parameters
mjd1,m1= np.genfromtxt('star1.txt',usecols= (0,1), unpack= True)
P1=float(1.154652**(-1))
P1 = float('%.6f'%(P1))
A1 = 0.256766344 #mag

mjd2,m2= np.genfromtxt('star2.txt',usecols= (0,1), unpack= True)
P2=float(2.05735129**(-1))
P2 = float('%.6f'%(P2))
A2 = 0.427443961 #mag

print P1
print P2
### Plotting

#For star1.txt
plt.title('Aparent magnitude vs. JD for star1.txt')
plt.ylabel('Aparent magnitude (m)')
plt.xlabel('JD')
plt.scatter(mjd1, m1, s=0.8, color = 'blue')
plt.savefig('star1txt_simple_plot.png', format = 'png')
plt.close()
#plt.figure(figsize=(7,7))

plt.title(r'Aparent magnitude vs. Phase for star1.txt')
plt.scatter(phase(mjd1, P1),m1, s = 1.2, color='red')
plt.xlabel('Phase')
plt.ylabel('Aparent Magnitude (m)')
plt.gca().invert_yaxis()
plt.savefig('star1txt_phase_plot.png', format = 'png')
plt.close()

#For star2.txt
plt.title('Aparent magnitude vs. JD for star2.txt')
plt.ylabel('Aparent magnitude (m)')
plt.xlabel('JD')
plt.scatter(mjd2, m2, s= 0.8, color = 'red')
plt.savefig('star2txt_simple_plot.png', format = 'png')
plt.close()
#plt.figure(figsize=(7,7))

plt.title(r'Aparent magnitude vs. Phase for star2.txt')
plt.scatter(phase(mjd2, P2),m2, s = 1.2, color='black')
plt.xlabel('Phase')
plt.ylabel('Aparent Magnitude (m)')
plt.gca().invert_yaxis()
plt.savefig('star2txt_phase_plot.png', format = 'png')
plt.close()
