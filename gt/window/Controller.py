from gt.draw.VisGraph import Visgraph
from gt.window import GraphSim

class Controller:
    def __init__(self, window:GraphSim, visgraph:Visgraph) -> None:
        self.graph = visgraph
        self.win = window
        if not self.graph.lock:
            for ver in self.graph.vertices:
                self.graph.canvas.bind(ver.text,"<B1-Motion>",self.move_vertex)

    def move_vertex(self,event):
        ...