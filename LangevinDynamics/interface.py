import os
import click
@click.command()
@click.option('--x', prompt='Initial Position, x', help='Input initial position')
@click.option('--v', prompt='Initial Momentum, p', help='Input initial velocity')
@click.option('--temp', prompt='Temperature, T', help='Input Temperature')
@click.option('--lamda', prompt='Damping Coefficient , lambda', help='Input damping coefficient')
@click.option('--m', prompt='mass, m', help='Input mass')
@click.option('--dt', prompt='timestep, dt', help='Input timestep for the simulation')
@click.option('--steps', prompt='number of steps, N', help='Input timestep for the simulation')
@click.option('--o', default="out.dat" , help='Name of the output file')
@click.option('--i', prompt='Input file' , help='Name of the input file')
def start(x,p,temp,lamda,m,dt,steps,o,i):
    import LangevinDynamics as ld
    i = os.getcwd()+"/" + i
    ld.run(float(x),float(v)*float(m),float(m),float(temp),float(lamda),i,float(dt),int(steps),o)
if __name__ == '__main__':
        start()
