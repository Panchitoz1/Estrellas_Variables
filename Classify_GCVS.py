# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:18:55 2017

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
        result.append(x.split()[2])
f.close()
while '+195614.1' in result: result.remove('+195614.1')
while '+611248.9' in result: result.remove('+611248.9')
while '+195613.9' in result: result.remove('+195613.9')
while '+611249.3' in result: result.remove('+611249.3') 
mylist = list(set(result))
#print mylist
#print len(mylist)
letter_counts = Counter(result)
df = pandas.DataFrame.from_dict(letter_counts, orient='index') 
pandas.Series(Counter(result)).plot(kind='bar')
#plt.legend(loc='None') 
plt.ylabel('Object counts', size = 14)
plt.title('Variable Objects in each constellation (GCVS 5.1)')
print letter_counts
plt.text(1.5, 5000, r'Var. Objects = '+str(len(result)))
plt.show()
#plt.savefig('Histograma_constelaciones.png', format='png')
plt.close()
#'print mylist
print 'Done'  
print 'Total estrellas: ',len(result)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 

"""
lista_And, lista_Ant, lista_Aps = [], [], []
lista_Aqr, lista_Aql, lista_Ara = [], [], []
lista_Ari, lista_Aur, lista_Boo = [], [], []
lista_Cae, lista_Cam, lista_Cnc = [], [], []
lista_CVn, lista_CMa, lista_CMI = [], [], []
lista_Cap, lista_Car, lista_Cas = [], [], []
lista_Cen, lista_Cep, lista_Cet = [], [], []
lista_Cha, lista_Cir, lista_Col = [], [], []
lista_Com, lista_CrA, lista_CrB = [], [], []
lista_Crv, lista_Crt, lista_Cru = [], [], []
lista_Cyg, lista_Del, lista_Dor = [], [], []
lista_Dra, lista_Equ, lista_Eri = [], [], []
lista_For, lista_Gem, lista_Gru = [], [], []
lista_Her, lista_Hor, lista_Hya = [], [], []
lista_Hyi, lista_Ind, lista_Lac = [], [], []
lista_Leo, lista_LMi, lista_Lep = [], [], []
lista_Lib, lista_Lup, lista_Lyn = [], [], []
lista_Lyr, lista_Men, lista_Mic = [], [], []
"""