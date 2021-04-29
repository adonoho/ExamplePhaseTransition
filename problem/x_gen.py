#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi
Generating K-sparse signals of dimension n*1
"""

import random
import numpy as np
from problemSpec import problemInit


def x_generate(n, k):
    p = problemInit()
    x = np.zeros((n, 1))
    nonzero_loc = random.sample(range(n), k)
    for i in range(len(nonzero_loc)):
        x[nonzero_loc[i]] = 10 * np.abs(np.random.normal(p.mu, p.sigma, 1))

    return x
