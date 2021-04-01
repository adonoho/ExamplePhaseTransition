#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi
Manual Reduce Module
"""
import numpy as np
from numpy import linalg as LA
import random

import csv
import pandas as pd
import os
from numpy import empty
import glob
import sys, argparse
from collections import defaultdict
import os.path

n=100 #dimension of the signal

dir_name='/Users/mahsa/Desktop/Sample_Phase_transition/Results'


filename_suffix = 'txt'
indicator=0
M=30;


for i in range (1,n+1):
    if i>=1:
        if i==1:
            P1=empty([1,M]);

    base_foldername=str(i)
    base_filename='final_results'
    path=os.path.join(dir_name, base_foldername,base_filename+'.'+'txt' )
    path_origin=os.path.join(dir_name)
    FileCheckFlag=os.path.isfile(path)

    if FileCheckFlag==True:
        fout1=open('reduced_results.txt','a')
        fout1.write ("k,m,it,k/n,m/n,success_rate\n")
        fout2=open(path)

        for line in fout2:
            fout1.write(line)
            
        os.system('cat "reduced_results.txt" | tr -d "()" > "final_reduced_results.txt" ')   ##removig the ()
        fout1.close()
        fout2.close()
        indicator=indicator+1
print("Total number of folders with content is {x}".format(x=indicator))
    

  
