class QuickUnionUF(object):
    """QuickUnion Union Find"""
    id = []

    def __init__(self, n):
        if n < 0:
            raise ValueError("Argumento Inv�lido")

        # N acessos ao array
        self.id = [i for i in range(n)]

    def root(self, i):
        # Profundidade de i acessos ao array
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        # Profundidade de p e q acessos ao array
        return self.root(p) == self.root(q)

    def union(self, p, q):
        # Profundidade de p e q acessos ao array
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j

    def print(self):
        print(self.id)