import tkinter as tk

class VisEdge:
    def __init__(self, v1, v2, canvas: tk.Canvas) -> None:
        self.canvas = canvas
        self.e1 = v1
        self.e2 = v2
        self.line = canvas.create_line(*self.e1.coords, *self.e2.coords ,width=3)
        self.canvas.lower(self.line)


    def update(self,event=None):
        self.canvas.coords(self.line,*self.e1.coords, *self.e2.coords)
