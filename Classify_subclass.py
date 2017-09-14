# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 01:04:17 2017

@author: ffcarrasco
"""

import matplotlib.pyplot as plt
import pandas
from collections import Counter


file_name = 'gcvs5_copy.txt'
f=open(file_name,"r")
lines=f.readlines()
result=[]
for x in lines:
        result.append(x.split('|')[3])
f.close()
#print result
print([s.replace(' ', '') for s in result])
result = [s.replace(' ', '') for s in result]
#print result
#0 = [], [], [], [], []
variable_list = []

counter_UV, counter_RR, counter_SXARI, counter_N, counter_E = 0, 0, 0, 0, 0

for x in result:
    if x == 'UV' or x == 'RR' or x == 'SXARI' or x == 'N' or x == 'E':
        variable_list.append(x)
        if x == 'UV':
            counter_UV += 1
        elif x == 'RR':
            counter_RR += 1
        elif x == 'SXARI':
            counter_SXARI += 1
        elif x == 'N':
            counter_N += 1
        elif x == 'E':
            counter_E += 1
print variable_list
letter_counts = Counter(variable_list)
df = pandas.DataFrame.from_dict(letter_counts, orient='index') 
pandas.Series(Counter(variable_list)).plot(kind='bar')
#plt.legend(loc='None') 
plt.ylabel('Object counts', size = 14)
plt.title('Variable Objects detected (GCVS)')
print letter_counts
plt.text(0.2, 1300, r'Type E = '+str(counter_E))
plt.text(0.2, 1200, r'Type N = '+str(counter_E))
plt.text(0.2, 1100, r'Type RR = '+str(counter_RR))
plt.text(0.2, 1000, r'Type SXARI = '+str(counter_SXARI))
plt.text(0.2, 900, r'Type UV = '+str(counter_UV))
plt.savefig('Histograma_subclass.png', format = 'png')
#plt.savefig('Histograma_constelaciones.png', format='png')
plt.close()
#'print mylist
print 'Done'