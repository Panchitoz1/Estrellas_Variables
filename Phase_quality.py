# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 01:49:10 2017

@author: ffcarrasco
"""


import numpy as np
import matplotlib.pyplot as plt

def phase(mjd, P):  
    return (mjd/P)%1

def duplicate_list(lista):
    duplicated_list = []
    for x in xrange(0, 2*len(lista)):
        if x < len(lista):
            duplicated_list.append(lista[x])
        else: 
            duplicated_list.append(lista[x-len(lista)])
    return duplicated_list

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


colors = ['b', 'c', 'r', 'm', 'y']


#For star2.txt

plt.title(r'Different Phases for star1.txt (original is $P =$'+str(P1)+'$(d)$')
ax1 = plt.subplot(511)
a = plt.scatter(phase(mjd1, P1+0.0001),m1, s = 1.7, color=colors[0], marker = '+')
plt.setp(ax1.get_xticklabels(), fontsize=6)
plt.setp(ax1.get_yticklabels(), fontsize=6)
plt.gca().invert_yaxis()
ax2 = plt.subplot(512, sharex=ax1)
b = plt.scatter(phase(mjd1, P1+0.00001),m1, s = 1.7, color=colors[1], marker = 'x')
plt.setp(ax2.get_xticklabels(), fontsize=6)
plt.setp(ax2.get_yticklabels(), fontsize=6)
plt.gca().invert_yaxis()
ax3 = plt.subplot(513, sharex=ax1)
c = plt.scatter(phase(mjd1, P2),m1, s = 1.7, color=colors[2], marker = 'o')
plt.setp(ax3.get_xticklabels(), fontsize=6)
plt.setp(ax3.get_yticklabels(), fontsize=6)
plt.ylabel('Aparent Magnitude ($m_V$)')
plt.gca().invert_yaxis()
ax4 = plt.subplot(514, sharex=ax1)
d = plt.scatter(phase(mjd1, P1 - 0.00001),m1, s = 1.7, color=colors[3], marker = '8')
plt.setp(ax4.get_xticklabels(), fontsize=6)
plt.setp(ax4.get_yticklabels(), fontsize=6)
plt.gca().invert_yaxis()
ax5 = plt.subplot(515, sharex=ax1)
e = plt.scatter(phase(mjd1, P1 - 0.0001),m1, s = 1.7, color=colors[4], marker = 'D')
plt.setp(ax5.get_xticklabels(), fontsize=6)
plt.setp(ax5.get_yticklabels(), fontsize=6)
plt.xlabel('Phase')
plt.gca().invert_yaxis()
plt.legend((a, b, c, d, e),
           ('P+0.0001', 'P+0.00001', 'P+0', 'P-0-00001', 'P-0.0001'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)


plt.savefig('star2txt_phase_quality.png', format = 'png')
plt.close()


#For star2.txt

plt.title(r'Different Phases for star1.txt (original is $P =$'+str(P2)+'$(d)$')
ax1 = plt.subplot(511)
a = plt.scatter(phase(mjd2, P2+0.0001),m2, s = 1.7, color=colors[0], marker = '+')
plt.setp(ax1.get_xticklabels(), fontsize=6)
plt.setp(ax1.get_yticklabels(), fontsize=6)
plt.gca().invert_yaxis()
ax2 = plt.subplot(512, sharex=ax1)
b = plt.scatter(phase(mjd2, P2+0.00001),m2, s = 1.7, color=colors[1], marker = 'x')
plt.setp(ax2.get_xticklabels(), fontsize=6)
plt.setp(ax2.get_yticklabels(), fontsize=6)
plt.gca().invert_yaxis()
ax3 = plt.subplot(513, sharex=ax1)
c = plt.scatter(phase(mjd2, P2),m2, s = 1.7, color=colors[2], marker = 'o')
plt.setp(ax3.get_xticklabels(), fontsize=6)
plt.setp(ax3.get_yticklabels(), fontsize=6)
plt.ylabel('Aparent Magnitude ($m_V$)')
plt.gca().invert_yaxis()
ax4 = plt.subplot(514, sharex=ax1)
d = plt.scatter(phase(mjd2, P2 - 0.00001),m2, s = 1.7, color=colors[3], marker = '8')
plt.setp(ax4.get_xticklabels(), fontsize=6)
plt.setp(ax4.get_yticklabels(), fontsize=6)
plt.gca().invert_yaxis()
ax5 = plt.subplot(515, sharex=ax1)
e = plt.scatter(phase(mjd2, P2 - 0.0001),m2, s = 1.7, color=colors[4], marker = 'D')
plt.setp(ax5.get_xticklabels(), fontsize=6)
plt.setp(ax5.get_yticklabels(), fontsize=6)
plt.xlabel('Phase')
plt.gca().invert_yaxis()
plt.legend((a, b, c, d, e),
           ('P+0.0001', 'P+0.00001', 'P+0', 'P-0-00001', 'P-0.0001'),
           scatterpoints=1,
           loc='upper left',
           ncol=3,
           fontsize=8)


plt.savefig('star2txt_phase_quality.png', format = 'png')
plt.close()
