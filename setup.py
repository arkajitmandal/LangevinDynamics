from distutils.core import setup

setup(name='Langevin Dynamics Simulator',
      version='0.01',
      description='A 1D langevin simulator',
      author='Arkajit Mandal',
      author_email="arkajitmandal@rochester.edu",
      url='https://github.com/arkajitmandal',
      packages=["LangevinDynamics"],

      entry_points = { 
          'console_scripts' : ['langevin = LangevinDynamics.start:go']
          }
      )

    
