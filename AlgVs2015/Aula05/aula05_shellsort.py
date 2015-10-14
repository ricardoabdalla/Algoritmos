from aula05_util import *
from math import floor

class Shell(object):
    """Implementação de ordenação por Shell Sort"""

    def sort(self, colecao):
        n = len(colecao)
        h = 1

        while h < (n / 3):
            h = 3 * h + 1 # 1, 4, 13, 40

        while h >= 1:
            for i in range(h, n):
                j = i
                while j >= h and menor(colecao[j], colecao[j - h]):                    
                    troca(colecao, j, j - h)
                    j -= h

            h = floor(h / 3) 