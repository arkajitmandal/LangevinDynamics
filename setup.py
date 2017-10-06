from distutils.core import setup

with open('README.md') as f:
        long_description = ''.join(f.readlines())

with open('requirements.txt') as f:
        all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x] 

setup(name='Langevin Dynamics Simulator',
      version='0.02',
      description='A 1D langevin simulator',
      long_description=long_description,
      author='Arkajit Mandal',
      author_email="arkajitmandal@rochester.edu",
      url='https://github.com/arkajitmandal',
      packages=["LangevinDynamics"],
      install_requires=install_requires,
      entry_points = { 
          'console_scripts' : ['langevin = LangevinDynamics.show:start']
          }
      )

    
