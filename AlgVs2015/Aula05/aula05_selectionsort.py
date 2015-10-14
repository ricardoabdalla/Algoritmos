from aula05_util import *

class Selection(object):
    """Implementação de ordenação por Selection Sort"""

    def sort(self, colecao):
        n = len(colecao)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if menor(colecao[j], colecao[min]):
                    min = j
            troca(colecao, i, min)
