from aula05_util import *
from math import floor

class Merge(object):
    """Implementação de ordenação por Merge Sort"""

    def merge(self, colecao, aux, low, mid, high):
        for k in range(low, high + 1):
            aux[k] = colecao[k]
        i = low
        j = mid + 1
        for k in range(low, high + 1):
            if i > mid:
                colecao[k] = aux[j]
                j += 1
            elif j > high:
                colecao[k] = aux[i]
                i += 1
            elif menor(aux[j], aux[i]):
                colecao[k] = aux[j]
                j += 1
            else:
                colecao[k] = aux[i]
                i += 1

    def __sort__(self, colecao, aux, low, high):
        if high <= low:
            return
        mid = floor(low + (high - low) / 2)
        self.__sort__(colecao, aux, low, mid)
        self.__sort__(colecao, aux, mid + 1, high)
        self.merge(colecao, aux, low, mid, high)

    def sort(self, colecao):
        aux = []
        for i in range(len(colecao)):
            aux.append(None)
        self.__sort__(colecao, aux, 0, len(colecao) -1)      