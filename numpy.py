# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 15:32:14 2017

@author: Bhaskar Karn
"""

import numpy as np
from numpy import array
c=[1,5,8]
np.sum(c)
height=[1,2,3,4,5,6]
weight=[6,7,8,9,2,3]
np_height=np.array(height)
np_weight=np.array(weight)
np_weight/np_height**2
bmi=np_weight/np_height**2
np.round(bmi,1)
print(bmi)
np.array([2,"is", True])
bmi=np.array([1,2,3,4])
bmi[2]
bmi>2
bmi[bmi>23]
type(np_height)
type(np_weight)
