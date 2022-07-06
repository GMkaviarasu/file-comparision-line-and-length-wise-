Example:1

import os
import sys
import pandas as pd
import numpy as np

with open ('doc4.txt') as f1:
    d1=f1.readlines()

import regex as re
p1=re.compile(r'name:\b[a-z]{9}$')
p2=re.compile(r'email:\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
p3=re.compile(r'emp.ID:\d{4}     Date of joining:[0-9]{2}/[0-9]{2}/[0-9]{4}$')

dict1={0:p1,1:p2,2:p3}

def check(d1,dict1):
    for i,j in zip(dict1.keys(),dict1.values()):
        if re.match(j,d1[i]):
            pass
        else:
            print('wrong')
            print(d1[i])
    return 
check(d1,dict1)