![coverage image](./img/coverage.svg) 

Welcome to Langevin Dynamics
===

This is a 1 dimentional langevin dynamics simulator. 

## Installation
Download the zip, and cd to the directory where setup.py is located. 
On a very lucky day the following should work
```sh
$ pip3 install . 
```

## What do you need

A text file.

Required Files : a text file containing 4 columns. 
Each line have 4 columns; Index, position and the corresponding
velocity and force. 

This program will show an error if the particle moves beyond potential surface
given in your input file. For the forces corresponding to positions 
that are not exclusively written in the input file will be interpolated.


An example input file :

>1&nbsp;&nbsp;&nbsp;&nbsp;0.0&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;-1<br /> 
>2&nbsp;&nbsp;&nbsp;&nbsp;0.2&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;0<br />
>3&nbsp;&nbsp;&nbsp;&nbsp;0.4&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;0<br />
>4&nbsp;&nbsp;&nbsp;&nbsp;0.6&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;1<br /> 

So in the given example the particle at position = 0.1 will feel a force of -0.5 and if it evolves 
to position 0.7 or to -0.1 the program will exit will an error.


