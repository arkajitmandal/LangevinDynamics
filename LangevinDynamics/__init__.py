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

def getF_V(x,Data):
    """
    get the force at x by linear interpolation of Data
    Data is sorted herein
    """
    Data  = Data[Data[:,1].argsort()]
    xData = Data[:,1]
    vData = Data[:,2]
    fData = Data[:,3]
    minIndex = 0
    for i in range(len(xData)):
        if xData[i] <= x:
            minIndex = i
        else :
            break
    dx = xData[minIndex+1] - xData[minIndex]  
    dv = vData[minIndex+1] - vData[minIndex]  
    df = fData[minIndex+1] - fData[minIndex]  
    slopeF = df/dx 
    slopeV = dv/dx 
    Dx = x - xData[minIndex]
    V = vData[minIndex] + slopeV*Dx 
    F = fData[minIndex] + slopeF*Dx 
    return F,V
def verlet(x0,p0,m,Data,dt) :
    F1 , _  = getF_V(x0,Data) 
    x = x0 + p0*dt/m + (F1*dt**2)/(2*m)
    F2 , _  = getF_V(x,Data)
    p = p0 + (F1+F2)*dt/2
    return  x , p 

