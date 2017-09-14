# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 17:01:17 2017

@author: ffcarrasco
"""

import matplotlib.pyplot as plt
import pandas
from collections import Counter


file_name = 'gcvs5_copy.txt'
f=open(file_name,"r")
lines=f.readlines()
result_constellation=[]
result_classes = []
counter_eruptive_Sgr = 0
counter_pulsating_Sgr = 0
counter_rotating_Sgr = 0 
counter_cataclysmic_Sgr = 0 
counter_eclipsing_Sgr = 0
counter_others_Sgr = 0

counter_eruptive_Cae = 0
counter_pulsating_Cae = 0
counter_rotating_Cae = 0 
counter_cataclysmic_Cae = 0 
counter_eclipsing_Cae = 0
counter_others_Cae = 0

for x in lines:
        a = x.split()[2]
        b = x.split('|')[3]
        b = b.replace(" ", "")
        #We define conditions for variability classes
        cond_string_eruptive = (b == 'FU' or b == 'GCAS' or b == 'I' 
           or b == 'IA' or b == 'IB'or b == 'IN' or b == 'INA' 
           or b == 'INB' or  b == 'INT'or b == 'IT' or b == 'IN(YY)' 
           or b == 'ISA' or b == 'ISB' or b == 'RCB' or b == 'RS' 
           or b == 'SDOR' or b == 'UV' or b == 'UVN' or b == 'WR')
        cond_string_pulsating = (b == 'ACYG' or  b == 'BCEP' or b == 'BCEPS'
           or b == 'CEP' or b == 'CEP(B)' or b == 'CW' or b == 'CWA'
           or b == 'CWB' or b == 'DCEP' or b == 'DCEPS' or b == 'DSCT'
           or b == 'DSCTC' or b == 'GDOR' or b == 'L' or b == 'LB' 
           or b == 'LC' or b == 'M' or b == 'PVTEL' or b == 'RPHS' 
           or b == 'RR' or b == 'RR(B)' or b == 'RRAB' or b == 'RRC'
           or b == 'RV' or b == 'RVA' or b == 'RVB' or b == 'SR' 
           or b == 'SRA' or b == 'SRB' or b == 'SRC' or b == 'SRD' 
           or b == 'SXPHE' or b == 'ZZ' or b == 'ZZA' or b == 'ZZB')
        cond_string_rotating = (b == 'ACV' or b == 'ACVO' or b == 'BY'
           or b == 'ELL' or b == 'FKCOM' or b == 'PSR' or b == 'SXARI')
        cond_string_cataclysmic = (b == 'N' or b == 'NA' or b == 'NB' 
           or b == 'NC' or b == 'NL' or b == 'NR' or b == 'SN' 
           or b == 'SNI' or b == 'SNII' or b == 'UG' or b == 'UGSS'
           or b == 'UGSU' or b == 'UGZ' or b == 'ZAND')
        cond_string_eclipsing = (b == 'E' or b == 'EA' or b == 'EB'
           or b== 'EW'  or b == 'GS' or b ==  'PN' or b == 'RS'
           or b == 'WD' or b == 'WR' or b == 'AR' or b == 'D' 
           or b == 'DM' or b == 'DS' or b == 'DW' or b == 'K'
           or b == 'KE' or b == 'KW' or b == 'SD')
           
        if (a == 'Sgr' and cond_string_eruptive):
               counter_eruptive_Sgr += 1
        elif (a == 'Sgr' and cond_string_pulsating):
               counter_pulsating_Sgr += 1
        elif (a == 'Sgr' and cond_string_rotating):
            counter_rotating_Sgr += 1
        elif (a == 'Sgr' and cond_string_cataclysmic):
            counter_cataclysmic_Sgr += 1
        elif (a == 'Sgr' and cond_string_eclipsing):
            counter_eclipsing_Sgr += 1
        elif (a == 'Sgr' and not (cond_string_eruptive or 
             cond_string_pulsating or cond_string_rotating or 
             cond_string_cataclysmic or cond_string_eclipsing)):
            counter_others_Sgr += 1
        elif (a == 'Cae' and cond_string_eruptive):
               counter_eruptive_Cae += 1
        elif (a == 'Cae' and cond_string_pulsating):
               counter_pulsating_Cae += 1
        elif (a == 'Cae' and cond_string_rotating):
            counter_rotating_Cae += 1
        elif (a == 'Cae' and cond_string_cataclysmic):
            counter_cataclysmic_Cae += 1
        elif (a == 'Cae' and cond_string_eclipsing):
            counter_eclipsing_Cae += 1
        elif (a == 'Cae' and not (cond_string_eruptive or 
             cond_string_pulsating or cond_string_rotating or 
             cond_string_cataclysmic or cond_string_eclipsing)):
            counter_others_Cae += 1
            
classifications = ['Eruptive', 'Pulsating', 'Rotating', 'Cataclysmic', 'Eclipsing']
            
             
f.close()
print (counter_eruptive_Sgr+counter_pulsating_Sgr+counter_rotating_Sgr+
counter_cataclysmic_Sgr+ counter_eclipsing_Sgr + counter_others_Sgr)
print (counter_eruptive_Cae+counter_pulsating_Cae+counter_rotating_Cae+
counter_cataclysmic_Cae+ counter_eclipsing_Cae + counter_others_Cae)
results_Sgr = []
results_Sgr.append(counter_eruptive_Sgr)
results_Sgr.append(counter_pulsating_Sgr)
results_Sgr.append(counter_rotating_Sgr)
results_Sgr.append(counter_cataclysmic_Sgr)
results_Sgr.append(counter_eclipsing_Sgr)
results_Sgr.append(counter_others_Sgr)
print results_Sgr

results_Cae = []
results_Cae.append(counter_eruptive_Cae)
results_Cae.append(counter_pulsating_Cae)
results_Cae.append(counter_rotating_Cae)
results_Cae.append(counter_cataclysmic_Cae)
results_Cae.append(counter_eclipsing_Cae)
results_Cae.append(counter_others_Cae)
print results_Cae

lista_hist_Sgr = []
lista_hist_Cae = []
for x in xrange(0, counter_eruptive_Sgr):
    lista_hist_Sgr.append('Eruptive')
for x in xrange(0, counter_pulsating_Sgr):
    lista_hist_Sgr.append('Pulsating')
for x in xrange(0, counter_rotating_Sgr):
    lista_hist_Sgr.append('Rotating')
for x in xrange(0, counter_cataclysmic_Sgr):
    lista_hist_Sgr.append('Cataclys.')
for x in xrange(0, counter_eclipsing_Sgr):
    lista_hist_Sgr.append('Eclipsing')
for x in xrange(0, counter_others_Sgr):
    lista_hist_Sgr.append('Others')
for x in xrange(0, counter_eruptive_Cae):
    lista_hist_Cae.append('Eruptive')
for x in xrange(0, counter_pulsating_Cae):
    lista_hist_Cae.append('Pulsating')
for x in xrange(0, counter_rotating_Cae):
    lista_hist_Cae.append('Rotating')
for x in xrange(0, counter_cataclysmic_Cae):
    lista_hist_Cae.append('Cataclys.')
for x in xrange(0, counter_eclipsing_Cae):
    lista_hist_Cae.append('Eclipsing')
for x in xrange(0, counter_others_Cae):
    lista_hist_Cae.append('Others')


letter_counts = Counter(lista_hist_Sgr)
df = pandas.DataFrame.from_dict(letter_counts, orient='index') 
pandas.Series(Counter(lista_hist_Sgr)).plot(kind='bar', color = 'red')
plt.xticks(rotation=0)
plt.ylabel('Variable Objects counts', size = 14)
plt.title('Distribution for Variable Obj. in Sgr const. (GVCS 5.1)')
plt.text(0.1, 4000, r'Eruptive Obj.: '+str(counter_eruptive_Sgr))
plt.text(0.1, 3800, r'Pulsating Obj.: '+str(counter_pulsating_Sgr))
plt.text(0.1, 3600, r'Rotating Obj.: '+str(counter_rotating_Sgr))
plt.text(0.1, 3400, r'Cataclysmic Obj.: '+str(counter_cataclysmic_Sgr))
plt.text(0.1, 3200, r'Eclipsing Obj.: '+str(counter_eclipsing_Sgr))
plt.text(0.1, 3000, r'Others Obj.: '+str(counter_others_Sgr))
plt.savefig('Sgr_variable_dist.png', format = 'png')
plt.close()

letter_counts = Counter(lista_hist_Cae)
df = pandas.DataFrame.from_dict(letter_counts, orient='index') 
pandas.Series(Counter(lista_hist_Cae)).plot(kind='bar', color = 'yellow')
plt.xticks(rotation=0)
plt.ylabel('Variable Objects counts', size = 14)
plt.title('Distribution for Variable Obj. in Cae const. (GVCS 5.1)')
plt.text(0.1, 14, r'Eruptive Obj.: '+str(counter_eruptive_Cae))
plt.text(0.1, 13, r'Pulsating Obj.: '+str(counter_pulsating_Cae))
plt.text(0.1, 12, r'Rotating Obj.: '+str(counter_rotating_Cae))
plt.text(0.1, 11, r'Cataclysmic Obj.: '+str(counter_cataclysmic_Cae))
plt.text(0.1, 10, r'Eclipsing Obj.: '+str(counter_eclipsing_Cae))
plt.text(0.1, 9, r'Others Obj.: '+str(counter_others_Cae))
plt.ylim(0, 17)
plt.savefig('Cae_variable_dist.png', format = 'png')
plt.close()