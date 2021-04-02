#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi
Generating K-sparse signals of dimension n*1
"""

import random
import numpy as np
from ProblemSpec import ProblemInit


def X_generate(n,k):
    I=ProblemInit()
    X=np.zeros((n,1))
    nonzero_loc=random.sample(range(n),k)
    for i in range(len(nonzero_loc)):
        X[nonzero_loc[i]]=10*np.abs(np.random.normal(I.mu,I.sigma,1))

    return X
