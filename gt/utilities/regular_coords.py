from math import pi, sin, cos
import numpy as np

def regular_coords(graph):
    ang = 2*pi/len(graph.vertices)
    base = np.array((0,1))
    return {
        vertex: np.dot(np.array((
            (cos(i*ang),-sin(i*ang)),
            (sin(i*ang),cos(i*ang))
        )),base) for i,vertex in enumerate(graph.vertices)
    }

def main():
    ...

if __name__ == "__main__":
    main()