from aula05_util import *

class Insertion(object):
    """Implementação de ordenação por Insertion Sort"""

    def sort(self, colecao):
        n = len(colecao)
        for i in range(n):
            for j in range(i, 0, -1):
                if menor(colecao[j], colecao[j-1]):
                    troca(colecao, j, j-1)
                else:
                    break
            