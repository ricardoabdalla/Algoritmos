class QuickFindUF(object):
    """QuickFind Union Find"""
    id = []

    def __init__(self, n):
        if n < 0:
            raise ValueError("Argumento Inválido")

        # N acessos ao array
        self.id = [i for i in range(n)]

    def connected(self, p, q):
        # 2 acessos ao array
        return self.id[p] == self.id[q]

    def union(self, p, q):
        # No pior caso, 2N + 2 acessos ao array
        pId = self.id[p]
        qId = self.id[q]
        for i in range(len(self.id)):
            if self.id[i] == pId:
                self.id[i] = qId

    def print(self):
        print(self.id)