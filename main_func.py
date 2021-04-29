#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: mahsa lotfi
Main module for phase transition
"""

from dask import delayed, compute, persist, visualize
from dask.distributed import Client, LocalCluster, wait, as_completed
from problem.problemSpec import problemInit
from problem.loop import inner_loop

gClient = None
# gRange = 99
gRange = 12


def phase_transition():
    p = problemInit()
    m = p.m
    loop = delayed(inner_loop)

    # results = []
    # for i in range(gRange):
    #     result = loop(int(m[i]))
    #     results.append(result)
    loops = [loop(int(m[i])) for i in range(gRange)]
    # visualize(loops, filename='delayed_results', format='svg')
    futures = gClient.compute(loops)
    wait(futures)
    # for future in futures:
    #     print(future.result)
    for future, result in as_completed(futures, with_results=True):
        print(result)
    # print(results)


if __name__ == "__main__":
    cluster = LocalCluster(dashboard_address='localhost:8787')
    gClient = Client(cluster)
    phase_transition()
