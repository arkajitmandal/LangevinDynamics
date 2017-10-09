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
    
def test_getF():  
    Data = np.array([[1,2, 3, 4] , [2, 5, 4, 6]])
    F = ld.getF(3.5,Data)
    assert (np.isclose(F,5.0)) , "Interpolation of F is wrong"


def test_Verlet():
    import random
    T = 5.0
    lamda = 0.0
    x0 =  1 + random.random()
    p0 = random.random()
    F = 0.0
    m = 1.0
    dt = 0.2
    Data = np.array([[1,0,0,0],[2,2,0,0],[3,5,0,0],[4,10,0,0]])
    x, p = ld.verlet(x0,p0,m,Data,dt,T,lamda)
    assert (p0 == p) , "Verlet introducing spurious force"
    assert (x0 != x) or (p0 == 0.0) , "Position should change"

def test_randomForce():
    T = 5.0
    lamda = 0.0
    F = ld.randomForce(T,lamda)
    assert (F == 0.0) , "The distribution should become Delta function in this limit"
    T = 0.001
    F = 0
    lamda = 0.1
    F = ld.randomForce(T,lamda) 
    assert (F != 0.0) ,  "random force not generated"
    for i in range(1000):
        F +=  ld.randomForce(T,lamda)
    print( F)
    assert (F <1), "average random force must be small"

def test_dampingForce():
    F = ld.dampingForce(5,2,1 )
    assert F == -10, "Error in Damping Force"
    import random
    F = ld.dampingForce(random.random(),0,random.random() )
    assert F == 0 , "Spurious Damping Force!!"

def test_run():
    Data = [False,np.array([[1,0,0,0],[2,2,0,0],[3,5,0,0],[4,10,0,0]])]
    import random
    x = random.random()
    Out = ld.run(x,0,2,0,0,Data,0.1,2,".useless")
    assert  ( len(Out) ==3 ), "Number of steps ran is not correct"
    assert  (Out[-1][1] == x ) ,"Propagation Error"
    p = random.random()
    Out = ld.run(x,p,2,0,0,Data,0.1,2,".useless")
    assert  np.isclose(Out[-1][1] , x+ (p*0.1)) , "Propagation not Correct"

def test_interface():
    import click
    from click.testing import CliRunner
    from LangevinDynamics import interface as inter
    runner = CliRunner()
    result = runner.invoke(inter.start, ["--x", "0" , "--v" ,  "1","--temp" ,"1" , "--lamda", "1","--m" , "1","--dt","0.1","--steps" ,"10", "--o",".useless","--i", "Test"]   )
    assert  result.output.split("\n")[0] == "Test", "console command not working" 

def test_gui():
    from LangevinDynamics import gui_interface as gui
    f = gui.gui(["x","p"],False)
    assert len(f[0]) == len(f[1]), "Number of entrybox should be equal to number of labels"
