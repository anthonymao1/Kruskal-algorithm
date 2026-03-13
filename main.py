class DisjointSet:
    def __init__(self, vertices):
        self.parent = {v: v for v in vertices}

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            self.parent[rootY] = rootX

def kruskal(vertices, edges):
    ds = DisjointSet(vertices)
    mst = []
    edges = sorted(edges, key=lambda x: x[2])

    for u, v, w in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, w))
    return mst

if __name__ == "__main__":
    vertices = ["A","B","C","D"]
    edges = [
        ("A","B",1),
        ("B","C",3),
        ("A","C",2),
        ("C","D",4)
    ]

    print("Edges in MST:", kruskal(vertices, edges))
