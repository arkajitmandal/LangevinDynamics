import numpy
import io
def test_import():
    import LangevinDynamics
def test_read():
    import LangevinDynamics as ld
    mytxt = u"""1 0.1 5 5
    2 0.2 6 6"""
    myFile = io.StringIO(mytxt)
    dat = ld.read(myFile)
    assert (dat[0][0] == 1.0) , "data not read properly" 

