###Example:1 (length wise file comparison)

import os
import sys
file1 = open("BACSoutput.txt", "r")

d = file1.readlines()
 
length = []
# Strips the newline character
for line in d:
    length.append(len(line))

l1=[81, 61, 81, 81, 96, 102, 102, 102, 101, 84, 82, 59]

def compare_length(d,l1):
    l=[]
    for i in range(len(d)):
        l.append(len(d[i]))
        
    if l==l1:
    
        print('pass')
    else:
        print('fail')
    return

compare_length(d,l1)
print(length)

###Example: 2 (File comparision - line wise)
import os
import sys
import pandas as pd
import numpy as np

with open ('BACSoutput.txt') as f1:
    d1=f1.readlines()

import regex as re
p0=re.compile(r'[A-Z]{3}+\d+[A-Z]{3}\d{4}+[\s]{30}+\d{6}+[\s]{32}+\d{1}$')
p1=re.compile(r'[A-Z]{3}+\d{1}+[A-Z]{1}+\d{6}+[A-Z]{1}+\d{9}+[A-Z]{3}+\d{11}+[\s]{7}+\d{5}+[\s]{1}+\d{12}$')
p2=re.compile(r'[A-Z]{3}+\d{1}+\w{1}+\d{10}+[\s]{35}+\d{2}+[\s]{28}$')
p3=re.compile(r'[A-Z]{3}+\d{1}+[\s]{1}+\d{11}+[\s]{4}+\d{9}+[\s]{1}+[A-Za-z]{5}+[\s]{2}+\d{3}+[\s]{40}$')
p4=re.compile(r'\d+[A-Z]{1}+\d{15}+[A-Z]{1}+\d{6}+[\s]{8}+[A-Z]{2}+[\s]{2}+[A-Z]{1}+[\s]{1}+[A-Z]{1}+[\s]{1}+[A-Z]{7}+[\s]{4}+\d{8}+[/]+\d{9}+[A-Z]{3}+[\s]{1}+\d{8}$')
p5=re.compile(r'\d+[A-Z]{1}+\d{15}+[A-Z]{1}+\d{6}+[\s]{8}+[A-Z]{2}+[\s]{2}+[A-Z]{1}+[\s]{1}+[A-Z]{1}+[\s]{1}+[A-Z]{7}+[\s]{4}+\d{8}+[/]+\d{9}+[A-Z]{3}+[\s]{1}+\d{8}+[\s]{6}$')
p6=re.compile(r'\d+[A-Z]{1}+\d{15}+[A-Z]{1}+\d{6}+[\s]{8}+[A-Z]{2}+[\s]{2}+[A-Z]{1}+[\s]{1}+[A-Z]{1}+[\s]{1}+[A-Z]{7}+[\s]{4}+\d{8}+[/]+\d{9}+[A-Z]{3}+[\s]{1}+\d{8}+[\s]{6}$')
p7=re.compile(r'\d+[A-Z]{1}+\d{15}+[A-Z]{1}+\d{6}+[\s]{8}+[A-Z]{2}+[\s]{2}+[A-Z]{1}+[\s]{1}+[A-Z]{1}+[\s]{1}+[A-Z]{7}+[\s]{4}+\d{8}+[/]+\d{9}+[A-Z]{3}+[\s]{1}+\d{8}+[\s]{6}$')
p8=re.compile(r'\d{6}+[\s]{8}+\d{9}+[\s]{12}+\d{3}+[\s]{26}+[A-Z]{6}+[\s]{12}+[A-Z]{2}+[\s]{1}+[A-Z]{1}+[\s]{1}+[A-Z]{1}+[\s]{1}+[A-Z]{7}+[\s]{4}$')
p9=re.compile(r'[A-Z]{3}+\d{1}+[A-Z]{1}+\d{6}+[A-Z]{1}+\d{9}+[A-Z]{3}+\d{11}+[\s]{7}+\d{5}+[\s]{1}+\d{24}+[\s]{11}$')
p10=re.compile(r'[A-Z]{3}+\d{1}+[A-Z]{1}+\d{10}+[\s]{35}+\d{2}+[\s]{29}$')
p11=re.compile(r'[A-Z]{3}+\d{4}+[\s]{10}+\d{3}+[\s]{10}+\d{1}+[\s]{6}+\d{7}+[\s]{8}+\d{7}$')


dict1={0:p0,1:p1,2:p2,3:p3,4:p4,5:p5,6:p6,7:p7,8:p8,9:p9,10:p10,11:p11}

def check(d1,dict1):
    for i,j in zip(dict1.keys(),dict1.values()):
        if re.match(j,d1[i]):
            pass
        else:
            print('Pattern Not Mach')
            print(d1[i])
    return 
check(d1,dict1)