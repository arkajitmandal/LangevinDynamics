"""This is the code for Langevin Dynamics"""
import numpy as np 

def read(fob):
    """
    reads a text file with space separated values
    it assumes first column as x and second column as V(x)
    returns a 2D numpy array 
    """
    dat = fob.readlines()
    lines = []
    for i in dat:
        lines+= i.replace("\n","").split()
    Column =  len(i.replace("\n","").split())    
    Data = np.array(lines,"float")    
    Data.shape = (len(dat),Column)
    return Data 

def getForce(x,Data):
    return 0
