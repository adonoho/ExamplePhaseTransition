#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: mahsa lotfi
Inner loop subroutine
"""
import numpy as np
from numpy import linalg as LA
import random
import csv
import time
from ProblemSpec import ProblemInit
from X_gen import X_generate
from opt_func import optimization_function

def inner_loop(m):
   S=ProblemInit()
   n=S.n
   it=S.Monte_Carlo_iter
   mu=S.mu
   sigma=S.sigma

   for k in range (1,n+1):
               A=np.random.normal(mu, sigma, (m,n))
               if k==1:
                   Success=np.zeros((it,1))
               for i in range (0,it):
                   X=X_generate(n,k)
                   X_hat=optimization_function(A,X,m)
                   err=LA.norm(X-X_hat,2)/LA.norm(X,2)
                   if err <= S.error_threshold:
                       Success[i]=1
               success_rate=np.sum(Success)/it
               print('s',success_rate) 
               output=k,m,it,k/n,m/n,success_rate
    
               outF=open("final_results.txt","a+")
               outF.writelines(str(output)+"\n")
               outF.close()
               if i==(it-1):
                       Success=np.zeros((it,1))
                       err=0
                       success_rate=0
      
