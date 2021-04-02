#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi
Main module for phase transition
"""


from ProblemSpec import ProblemInit
from loop import inner_loop

S=ProblemInit()
m=S.m


for i in range(99):              
    inner_loop(int(m[i]))
