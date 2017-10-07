![coverage image](./img/coverage.svg) 

Welcome to Langevin Dynamics
===

This is a 1 dimentional langevin dynamics simulator. 

Required Files : a text file containing 4 columns. 
Each line have 4 columns; Index, position and the corresponding
velocity and force. 

This program will show an error if the particle moves beyond potential surface
given in your input file. For the forces corresponding to positions 
that are not exclusively written in the input file will be interpolated.


An example input file :

>1 0.0 1 -1  \n
>2 0.2 2 0   \n
>3 0.4 2 0   \n
>4 0.6 1 1   \n

So in the given example the particle at position = 0.1 will feel a force of -0.5 and if it evolves 
to position 0.7 or to -0.1 the program will exit will an error.


