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

def verlet(x0,p0,m,Data,dt,T,lamda) :
    """
    Verlet algorithm for only for 1 step
    """
    F1 , _  = getF_V(x0,Data) 
    x = x0 + p0*dt/m + (F1*dt**2)/(2*m)
    F2 , _  = getF_V(x,Data)
    #Add random Force and Damping
    F1 += randomForce(T,lamda) + dampingForce(lamda,p0,m )
    F2 += randomForce(T,lamda) + dampingForce(lamda,p0,m )
    p = p0 + (F1+F2)*dt/2
    return  x , p 


def randomForce(T,lamda):
    """
    random force generetor
    """
    import random
    sigma = (T*lamda)**0.5
    F = random.gauss(0,sigma)
    return F

def dampingForce(lamda,p,m ):
    """
    Damping Force
    """
    return -lamda*p/m

def run(x,p,m,T,lamda,filename,dt,steps,out):
    if (out != False) :
        fob = open(out,"w+" )
    import os
    if (filename[0] != False):
        Data = read( open(filename,"r"))
    else:
        Data = filename[1]
    Out  = np.array([0,x,p])
    for t in range(int(steps)+1):
        x,p = verlet(x,p,m,Data,dt,T,lamda)
        Out = np.concatenate((Out,[dt*t,x,p])) 
        thisLine = '{: <20} \t {: <20} \t{: <20} \t{: <20}\n'.format(t+1,dt*(t+1),x,p)
        if (out !=False) :
            fob.writelines(thisLine)
    if (out !=False) :
        fob.close()    
    return Out
