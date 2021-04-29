#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi

Optimization Module

"""

import cvxpy as cp
import numpy as np

from problemSpec import problemInit


def optimization_function(A,X,m):
    p = problemInit()
    n = p.n

    # x_hat = np.zeros((n,1))
    y = np.matmul(A,X)

    z = cp.Variable(shape=(n,1))
    constraint = []
    constraint += [y == cp.matmul(A, z)]
    objective_func = cp.Minimize(cp.norm(z, p=1))
    opt_problem = cp.Problem(objective_func, constraint)
    opt_problem.solve(solver=cp.SCS, gpu=False, eps=10**(-5), verbose=False, use_indirect=False)
    x_hat = z.value
                      
    return x_hat

