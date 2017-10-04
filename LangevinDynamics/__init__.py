"""This is the code for Langevin Dynamics"""
import numpy as np 

def read(filename):
    """
    reads a text file with space separated values
    it assumes first column as x and second column as V(x)
    returns a 2D numpy array 
    """
    fob = open(filename,"r")
    dat = fob.readlines()
    lines = []
    for i in dat:
        lines+=i.replace("\n")
    Vx = np.array(lines,"float")    
    Vx.shape = (len(dat),2)
    return Vx 

