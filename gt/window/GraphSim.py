from gt.utilities.constants import WINDOW_WIDTH, WINDOW_HEIGHT
from gt.utilities import regular_coords,coord_plotter
from gt.draw.VisGraph import Visgraph
import tkinter as tk

class GraphSim:
    def __init__(self,graph,*,pre_plot = False) -> None:
        if graph.n > 15*graph.sfp_n and pre_plot:
            raise ValueError(f"Preplotting is only supported up to {15*graph.sfp_n} vertices for this graph.")
        self.root = self.make_win()
        self.canvas = self.make_canvas()
        point_builder = coord_plotter if pre_plot else regular_coords
        self.visgraph = Visgraph(self.canvas,graph,point_builder)
        self.lock = False

    def make_win(self):
        root = tk.Tk()
        root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+0+0")
        root.title("Graph Simulator")
        root.resizable(False, False)
        return root
    
    def make_canvas(self):
        return tk.Canvas(self.root,bg="white",height=WINDOW_HEIGHT,width=WINDOW_WIDTH)

    def update(self):
        self.canvas.pack()
        self.root.mainloop()