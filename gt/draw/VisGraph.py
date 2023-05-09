from gt.utilities.constants import POLYGON_RADIUS, WINDOW_CENTER
from gt.utilities import regular_coords
from gt.graph import SSG
from typing import Callable
from .VisVertex import VisVertex
from .VisEdge import VisEdge
import tkinter as tk



class Visgraph:
    def __init__(self, canvas: tk.Canvas, graph: SSG, point_builder: Callable) -> None:
        self.canvas = canvas
        self.vertices = [self.add_vertex(vertex,coord) for vertex,coord in point_builder(graph).items()]
        self.edges = self.build_edges(graph,self.vertices)

    def add_vertex(self, vertex, coord):
        return VisVertex(vertex,*(POLYGON_RADIUS*coord+WINDOW_CENTER),self.canvas)

    def build_edges(self,graph,visverts):
        conv = {ver:visver for ver,visver in zip(graph.vertices,visverts)}
        edges = []
        for ver,nhb in graph.adj_map.items():
            for adj in nhb:
                if ver < adj:
                    break
                edges.append(VisEdge(conv[ver],conv[adj],self.canvas))