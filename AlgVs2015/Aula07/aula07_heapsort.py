from math import floor

class Heap(object):
    """Implementação de Heap Sort com arrays"""

    def sink(self, colecao, k, n):
        while (2 * k) <= n:
            j = 2 * k
            if j < n and self.menor(colecao, j, j+1):
                j += 1
            if not self.menor(colecao, k, j):
                break
            self.troca(colecao, k, j)
            k = j

    def menor(self, colecao, i, j):
        i = int(i)
        j = int(j)
        if colecao[i-1] < colecao[j-1]:
            return True
        else:
            return False

    def troca(self, colecao, i, j):
        i = int(i)
        j = int(j)
        temp = colecao[i-1]
        colecao[i-1] = colecao[j-1]
        colecao[j-1] = temp

    def sort(self, colecao):
        n = len(colecao)

        for k in range(floor(n/2), 0, -1):
            self.sink(colecao, k, n) 

        while n > 1:
            self.troca(colecao, 1, n)
            n -= 1
            self.sink(colecao, 1, n)