from .visualization import SimVis, start_server
import asyncio
import numpy as np

def read_energy(input_file):
        return None, None

async def main(sv): # pragma: no cover
        #create a simple energy
        x = np.linspace(-1, 1, 100)
        y = x**2
        sv.set_energy(x, y)

        while True:
             v.set_position(np.random.random(1))
             await asyncio.sleep(0.5)



def start(): # pragma: no cover
        sv = SimVis()
        start_server(sv)
        asyncio.ensure_future(main(sv))
        loop = asyncio.get_event_loop()
        loop.run_forever()
