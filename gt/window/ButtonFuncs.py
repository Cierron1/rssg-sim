def lock_graph(graph):
    graph.bind = not graph.bind
    graph.lock_button.config(text = ("Lock Graph" if graph.bind else "Unlock Graph"))
    for visvertex in graph.visvertices:
        visvertex.bind = graph.bind

def screenshot(graph):
    root = graph.root
    canvas = graph.canvas
    x = root.winfo_rootx()+7
    y = root.winfo_rooty()+7
    xx = (x + canvas.winfo_width())*1.23
    yy = (y + canvas.winfo_height())*1.24
    return ImageGrab.grab(bbox=(x, y, xx, yy))

def save(graph):
    filetypes = [
        ("PNG",".png"),
        ("JPEG",".jpeg"),
        ("GIF",".gif"),
        ("All files","*")]
    directory = tk.filedialog.asksaveasfilename(title = "Save Graph as", 
                                                defaultextension=".png",
                                                filetypes = filetypes,
                                                initialdir=__file__)
    if directory:
        image = screenshot(graph)
        image.save(f"{directory}")

def copy_to_clipboard(graph):
    image = screenshot(graph)
    output = BytesIO()
    image.convert('RGB').save(output, 'BMP')
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

def save_graph(graph):
    filetypes = [("Pickle",".pickle")]
    directory = tk.filedialog.asksaveasfilename(title = "Save Graph Data as", 
                                                defaultextension=".pickle",
                                                filetypes = filetypes,
                                                initialdir=__file__)
    data = tuple(
        (vertex.name,) + vertex.coords
        for vertex in graph.visvertices
    )
    with open(f"{directory}",'wb') as f:
        pickle.dump((data,graph.adj_map), f)

def load_graph(graph:VisGraph):
    filename = tk.filedialog.askopenfilename(title = "Open Graph Data",
                                            filetypes = [("Pickle",".pickle")],
                                            initialdir = __file__)
    with open(filename,'rb') as f:
        loaded = pickle.load(f)
    vertices = []
    for vertex in loaded[0]:
        visver = Vertex(vertex[0])
        setattr(visver,"val",int(vertex[0]))   
        setattr(visver,"_x",vertex[1])   
        setattr(visver,"_y",vertex[2])
        vertices.append(visver)
    graph.canvas.delete('all')
    graph.vertices = vertices
    graph.adj_map = loaded[1]
    graph.visvertices = construct_points(vertices,graph.canvas)
    graph.visedges = graph.build_edges()
    graph.update()
    lock_graph(graph)
    lock_graph(graph)
    return loaded

def add_vertex(graph):
    val_list = [vertex.val for vertex in graph.vertices]
    new_vertex = Vertex(str(max(val_list) + min(val_list)))
    setattr(new_vertex,'val',max(val_list) + min(val_list))
    graph.add_vertex(new_vertex)
    graph.visvertices.append(VisVertex(new_vertex.name,*WINDOW_CENTER,graph.canvas))
    for vertex in graph.vertices:
        if is_sq_sum(vertex.val, new_vertex.val):
            graph.add_edge(Edge(new_vertex,vertex))
    graph.canvas.delete("edge")
    graph.visedges = graph.build_edges()
    graph.update()
    lock_graph(graph)
    lock_graph(graph)