#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi
Main module for phase transition
"""


import numpy as np
from numpy import linalg as LA
import random
import csv
from ProblemSpec import ProblemInit
from loop import inner_loop
from X_gen import X_generate
from opt_func import optimization_function



S=ProblemInit()
m=S.m


for i in range(99):              
    inner_loop(int(m[i]))
    
