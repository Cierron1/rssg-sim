import tkinter as tk
from gt.utilities import coords
from gt.utilities.constants import CIRCLE_RADIUS

class VisVertex:
    def __init__(self, vertex, x, y, canvas:tk.Canvas) -> None:
        self.vertex = vertex
        self.canvas = canvas
        self._x, self._y = x,y
        self.radius = CIRCLE_RADIUS
        self.circle = self.canvas.create_oval(*coords(x,y,self.radius),fill="white",outline="black",width=5)
        self.text = self.canvas.create_text(x,y,text=str(vertex),font=('Arial','12','bold'))
        self._bind = True

    @property
    def coords(self):
        return self._x,self._y

    @coords.setter
    def coords(self, new_coords):
        if not self._bind:
            self._x, self._y = new_coords
            self.canvas.coords(self.text,new_coords)
            self.canvas.coords(self.circle,*coords(self.x,self.y,self.radius))

    def __hash__(self) -> int:
        return hash(self.vertex)