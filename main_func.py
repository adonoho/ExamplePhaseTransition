#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Andrew W. Donoho based on work by Mahsa Lotfi
Main module for phase transition
"""

from dask import delayed
from dask.distributed import Client, wait, as_completed, LocalCluster
from dask_kubernetes import HelmCluster
from dask_cloudprovider.gcp import GCPCluster
# from problem.loop import inner_loop
# from problem.problemSpec import problemInit
import cvxpy as cp
import numpy as np
from numpy import linalg as la
import random


def problemInit():
    class ProbInit:
        def __init__(self):
            self.n = 100
            self.Monte_Carlo_iter = 30
            self.error_threshold = 10**(-2)
            self.m = np.linspace(2,self.n,self.n-1)
            self.mu = 0.0
            self.sigma = 1
    init = ProbInit()

    return init


def x_generate(n, k):
    p = problemInit()
    x = np.zeros((n, 1))
    nonzero_loc = random.sample(range(n), k)
    for i in range(len(nonzero_loc)):
        x[nonzero_loc[i]] = 10 * np.abs(np.random.normal(p.mu, p.sigma, 1))

    return x


def optimization_function(A, X, m):
    p = problemInit()
    n = p.n

    # x_hat = np.zeros((n,1))
    y = np.matmul(A, X)

    z = cp.Variable(shape=(n, 1))
    constraint = []
    constraint += [y == cp.matmul(A, z)]
    objective_func = cp.Minimize(cp.norm(z, p=1))
    opt_problem = cp.Problem(objective_func, constraint)
    opt_problem.solve(solver=cp.SCS, gpu=False, eps=10 ** (-5), verbose=False, use_indirect=False)
    x_hat = z.value

    return x_hat


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


# gRange = 99
gRange = 12


def phase_transition(client: Client):
    p = problemInit()
    m = p.m
    loop = delayed(inner_loop)

    loops = [loop(int(m[i])) for i in range(gRange)]
    # visualize(loops, filename='delayed_results', format='svg')
    futures = client.compute(loops)
    wait(futures)
    for future, result in as_completed(futures, with_results=True):
        print(result)


if __name__ == "__main__":
    # with GCPCluster(projectid='superb-garden-303018', machine_type='n1-standard-4', n_workers=2) as cluster:
    # with LocalCluster(dashboard_address='localhost:8787') as cluster:
    #     with Client(cluster) as client:
    #         phase_transition(client)
    cluster = HelmCluster(release_name='gke-dask')
    with Client(cluster) as client:
        phase_transition(client)
