from aula05_util import *
from math import floor
from random import shuffle

class Quick(object):
    """Implementação de ordenação por Quick Sort"""

    def partition(self, colecao, low, high):
        i = low
        j = high + 1

        while True:
            i += 1
            while menor(colecao[i], colecao[low]):
                if i == high: 
                    break
                i += 1

            j -= 1
            while menor(colecao[low], colecao[j]):
                if j == low: 
                    break
                j -= 1

            if i >= j:
                break

            troca(colecao, i, j)

        troca(colecao, low, j)
        return j

    def __sort__(self, colecao, low, high):
        if high <= low:
            return
        j = self.partition(colecao, low, high)
        self.__sort__(colecao, low, j-1)
        self.__sort__(colecao, j + 1, high)

    def sort(self, colecao):
        shuffle(colecao)
        self.__sort__(colecao, 0, len(colecao) -1)      