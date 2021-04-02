#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi

Initialization Routine
"""

import numpy as np


def ProblemInit():
    class ProbInit:
        def __init__(self):
            self.n=100;
            self.Monte_Carlo_iter=30;
            self.error_threshold=10**(-2)
            self.m=np.linspace(2,self.n,self.n-1)
            self.mu=0.0
            self.sigma=1
    Init=ProbInit();

    return Init;
