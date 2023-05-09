from dataclasses import dataclass,field
from gt.utilities.sfp_finder import is_ps, sfp

@dataclass(slots=True)
class SSG:
    k:int
    n:int = 0
    start_num:int = field(default=None,kw_only=True)
    adj_map: dict = field(init=False)
    sfp_n: int = field(init=False)

    def __post_init__(self) -> None:
        self.sfp_n = sfp(self.k) 
        if not self.start_num:
            self.start_num = self.k
        if self.n == 0:
            self.n = 15*sfp(self.sfp_n)
        self.adj_map = {self.start_num:[]} 
        for _ in range(1,self.n):
            self.add_vertex()
        # print(self.vertices)

    @property
    def vertices(self):
        return self.adj_map.keys()

    @property
    def name(self):
        return f"S_{len(self.vertices)}({self.k})"

    def add_vertex(self):
        new_vertex = max(self.vertices) + self.k
        self.adj_map[new_vertex] = []
        for vertex in self.vertices:
            self.add_edge(new_vertex, vertex)

    def add_edge(self, v1, v2):
        if is_ps(v2 + v1) and v1 != v2:
            if v1 not in self.adj_map[v2]:
                self.adj_map[v2].append(v1)
                self.adj_map[v1].append(v2)

    def __repr__(self) -> str:
        rep = f"V({self.name})={list(self.adj_map.keys())}"
        rep+=f"\n{self.name}="+"{\n"
        for key,value in self.adj_map.items():
            rep+=f"\t{key}:{value},\n"
        rep+="}"
        return rep