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
from problem.loop import inner_loop
from problem.problemSpec import problemInit

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
    # with LocalCluster(dashboard_address='localhost:8787') as cluster:
    # with GCPCluster(projectid='superb-garden-303018', machine_type='n1-standard-4', n_workers=2) as cluster:
    #     with Client(cluster) as client:
    #         phase_transition(client)
    cluster = HelmCluster(release_name='gke-dask')
    with Client(cluster) as client:
        phase_transition(client)
