#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: mahsa lotfi
Inner loop subroutine
"""
import numpy as np
from numpy import linalg as la
from problemSpec import problemInit
from x_gen import x_generate
from opt_func import optimization_function


def inner_loop(m: int) -> [(int, int, int, float, float, float)]:
    p = problemInit()
    n = p.n
    it = p.Monte_Carlo_iter
    mu = p.mu
    sigma = p.sigma

    result = []
    success = np.zeros((it, 1))
    for k in range(1, n+1):
        a = np.random.normal(mu, sigma, (m, n))
        for i in range(0, it):
            x = x_generate(n, k)
            x_hat = optimization_function(a, x, m)
            err = la.norm(x - x_hat, 2) / la.norm(x, 2)
            if err <= p.error_threshold:
                success[i] = 1
        result.append((k, m, it, k/n, m/n, np.sum(success)/it))
        success = np.zeros((it, 1))
    return result
