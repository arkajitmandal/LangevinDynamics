import numpy as np
import io
import LangevinDynamics as ld
def test_import():
    import LangevinDynamics
def test_read():
    import random
    a= random.randint(0,100)
    b= random.randint(0,100)
    c= random.randint(0,100)
    d= random.randint(0,100)
    mytxt = u"""1 %s %s 5
    2 %s %s 6"""%(a,b,c,d)
    myFile = io.StringIO(mytxt)
    dat = ld.read(myFile)
    assert (dat[0][0] == 1.0) , "data not read properly" 
    assert (dat[0][1] == a) , "data not read properly" 
    assert (dat[1][1] == c) , "data not read properly" 
    
def test_getForce():  
    Data = np.array([[1,2, 3, 4] , [2, 5, 4, 6]])
    F = ld.getForce(3.5,Data)
    assert (np.isclose(F,5.0))

