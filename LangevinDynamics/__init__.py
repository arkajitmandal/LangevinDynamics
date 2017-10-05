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
    """
    get the force at x by linear interpolation of Data
    Data is sorted herein
    """
    Data  = Data[Data[:,1].argsort()]
    xData = Data[:,1]
    fData = Data[:,3]
    minIndex = 0
    F = False
    for i in range(len(xData)):
        if xData[i] <= x:
            minIndex = i
        else :
            break
    dx = xData[minIndex+1] - xData[minIndex]  
    df = fData[minIndex+1] - fData[minIndex]  
    slope = df/dx 
    Dx = x - xData[minIndex]
    F = fData[minIndex] + slope*Dx 
    return F

