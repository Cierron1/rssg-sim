from gt.utilities.info import jelly, jug, totem, n,m, s
from gt.utilities import sfp
from gt.utilities.constants import COMP_SPACE
import numpy as np

def make_shifts(sfp_n):
    if sfp_n == 1:
        return [np.array((0,0))]
    shifts = [n/m]
    if sfp_n % 2 == 0:
        shifts.append(s)
    if sfp_n > 2:
        no_of_totems = (sfp_n-2)//2 if sfp_n%2 == 0 else (sfp_n-1)//2
        for _ in range(no_of_totems):
            shifts.append(1.5)

    shifts = np.array(shifts)

    diams = np.insert(np.delete(shifts,-1),0,0)

    pads = np.repeat(COMP_SPACE,len(shifts))
    pads[0] = 0

    offset = 0.5*(2*np.sum(shifts) + np.sum(pads))
    offset = np.repeat(offset, len(shifts))

    diams = 2*np.cumsum(diams)
    pads = np.cumsum(pads)

    shifts = shifts + diams + pads - offset
    shifts = [np.array((elem, 0)) for elem in shifts]
    
    return shifts

def coord_plotter(graph):
    ss_coords = dict()
    n = graph.k
    sfp_n = sfp(n)
    lsf_n = n//sfp_n
    cs_n = n*sfp_n
    
    shifts = make_shifts(sfp_n)

    scaled_jelly = {cs_n*key: value + shifts[0] for key,value in jelly.items()}
    ss_coords.update(scaled_jelly)
    del shifts[0]

    if sfp_n % 2 == 0:
        scaled_jug = {lsf_n*(sfp_n**2//4)*key : value + shifts[0] for key,value in jug.items()}
        ss_coords.update(scaled_jug)
        del shifts[0]
        
    if sfp_n > 2:
        no_of_totems = (sfp_n-2)//2 if sfp_n%2 == 0 else (sfp_n-1)//2
        for k in range(no_of_totems):
            scaled_totem = {
                lsf_n*(sfp_n**2*((key-1)//4)+sfp_n*(k+1))
                if key%4 == 1
                else lsf_n*(sfp_n**2*((key+1)//4)-sfp_n*(k+1))
                :value + shifts[0] for key,value in totem.items()}
            ss_coords.update(scaled_totem)
            del shifts[0]
    ss_coords = {key:value for key,value in ss_coords.items() if key <= max(graph.vertices)}
    ss_coords = dict(sorted(ss_coords.items()))
    return ss_coords
    
if __name__ == "__main__":
    ...