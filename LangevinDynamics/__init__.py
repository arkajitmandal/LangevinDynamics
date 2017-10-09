"""This is the code for Langevin Dynamics"""
import numpy as np 
import os
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

def getF(x,Data):
    """
    get the force at x by linear interpolation of Data
    Data is sorted herein
    """
    Data  = Data[Data[:,1].argsort()] # Data is sorted in case is not
    xData = Data[:,1]  
    fData = Data[:,3]
    minIndex = 0
    for i in range(len(xData)):
        if xData[i] <= x:
            minIndex = i
        else :
            break
    dx = xData[minIndex+1] - xData[minIndex]  
    df = fData[minIndex+1] - fData[minIndex]  
    slopeF = df/dx 
    Dx = x - xData[minIndex]
    F = fData[minIndex] + slopeF*Dx 
    return F

def verlet(x0,p0,m,Data,dt,T,lamda) :
    """
    Verlet algorithm for only for 1 step
    """
    F1  = getF(x0,Data) 
    x = x0 + p0*dt/m + (F1*dt**2)/(2*m) # First Part of Verlet
    F2  = getF(x,Data)
    #Add random Force and Damping
    F1 += randomForce(T,lamda) + dampingForce(lamda,p0,m ) # Force at t1
    F2 += randomForce(T,lamda) + dampingForce(lamda,p0,m ) # Force at t2
    p = p0 + (F1+F2)*dt/2   # Second part of Verlet
    return  x , p 


def randomForce(T,lamda):
    """
    random force generetor  
    T is Temperature
    lamda is the daming parameter
    Outputs random force
    """
    import random
    sigma = (T*lamda)**0.5 # Width of gaussian
    F = random.gauss(0,sigma)
    return F

def dampingForce(lamda,p,m ):
    """
    Damping Force 
    p is momentum
    m is mass
    """
    return -lamda*p/m

def run(x,p,m,T,lamda,filename,dt,steps,out):
    Result = [[0,x,p/m]]
    fob = open(out,"w+" )
    
    # The file input can be given either by a file
    # or as a Numpy array in the form => [False, [Youdata] ]
    # This feature is made so that this section can be tested
    
    if (filename[0] != False): 
        Data = read( open(filename,"r"))
    else:
        Data = filename[1]
    
    for t in range(int(steps)):
        x,p = verlet(x,p,m,Data,dt,T,lamda)
        thisLine = '{: <20} \t {: <20} \t{: <20} \t{: <20}\n'.format(t+1,dt*(t+1),x,p/m)
        fob.writelines(thisLine)
        Result += [[dt*(t+1),x,p/m ]]
    fob.close()  
    return Result 
