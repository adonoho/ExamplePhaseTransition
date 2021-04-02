#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi

Optimization Module

"""

import cvxpy as cp
import numpy as np

from ProblemSpec import ProblemInit


def optimization_function(A,X,m):
    I=ProblemInit()
    n=I.n

    X_hat=np.zeros((n,1))
    Y=np.matmul(A,X)

    z=cp.Variable(shape=(n,1))
    constraint =[]
    constraint +=[Y==cp.matmul(A,z)]
    objective_func=cp.Minimize(cp.norm(z,p=1))
    opt_problem=cp.Problem(objective_func,constraint)
    opt_problem.solve(solver=cp.SCS,gpu=False,eps=10**(-5),verbose=False,use_indirect=False)
    X_hat=z.value
                      
    return X_hat

