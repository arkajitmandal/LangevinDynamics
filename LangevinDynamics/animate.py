import click  # pragma: no cover
@click.command()  # pragma: no cover
@click.option("--o",prompt = "Your output file",help= "Your output file from langevin")  # pragma: no cover
@click.option("--i",prompt = "Your input file containing the potential",help= "Your output file from langevin")  # pragma: no cover
def show(traj,PES): # pragma: no cover
    import LangevinDynamics as ld
    import numpy as np
    import matplotlib.pyplot as plt
    import time
    import os
    pwd = os.getcwd()
    Traj = ld.read(open(pwd+"/"+traj,"r"))
    Pes  = ld.read(open(pwd+"/"+PES,"r")) 
    Pot  = np.array([Pes[:,1],Pes[:,2]])
    xmin = Pot[0][0]
    xmax = Pot[0][-1]
    ymin = np.min(Pot[1])
    ymax = np.max(Pot[1])
    step = Traj[:,1].size 
    plt.axis([xmin, xmax, ymax, ymin])
    plt.ion()
    for i in range(step):
        x = Traj[:,2][i]
        idx = (np.abs(Pes[:,1] - x)).argmin()        
        v   = Pot[1][idx]
        plt.clf()
        plt.plot(Pot[0],Pot[1])
        plt.scatter(x,v)
        plt.pause(0.05)
    while True:
        try:
            plt.pause(0.05)
        except :
            break 

