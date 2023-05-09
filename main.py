from gt.graph.SSG import SSG
from gt.window import GraphSim

def main():
    z = SSG(2,n=30)
    ss = GraphSim(z,pre_plot=True)
    ss.update()
    
if __name__ == "__main__":
    main()