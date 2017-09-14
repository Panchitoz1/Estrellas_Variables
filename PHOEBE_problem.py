# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 10:48:07 2017

@author: ffcarrasco
"""

import phoebe
from phoebe import u # units
import numpy as np
import matplotlib.pyplot as plt
import os

logger = phoebe.logger()

b = phoebe.default_binary()

#b['incl@orbit'] = 56.789

print b.get_value('mass@primary@component')

print b.save('test.phoebe')

#os.system('head -n 30 test.phoebe')
print b['mass@primary@component']

print b['mass@secondary@component']




b2 = phoebe.Bundle.open('test.phoebe')

print b2.get_value('incl@orbit')

