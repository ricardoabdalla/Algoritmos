from math import floor

class MaxPriorityQueue(object):
    """Implementação de Binary Heap com arrays"""

    __N = 0
    __items = []
    __capacity = 0

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacidade não pode ser nula ou negativa")
        self.__capacity = capacity + 1 # utilizando índice a partir de 1

        for i in range(self.__capacity):
            self.__items.append(None)

    def isEmpty():
        return self.__N == 0

    def swin(self, k):
        while k > 1 and self.menor(k / 2, k):
            self.troca(k, k / 2)
            k = floor(k / 2)

    def sink(self, k):
        while (2 * k) <= self.__N:
            j = 2 * k
            if j < self.__N and self.menor(j, j+1):
                j += 1
            if not self.menor(k, j):
                break
            self.troca(k, j)
            k = j

    def insert(self, key):
        self.__N += 1
        self.__items[self.__N] = key
        self.swin(self.__N)

    def delMax(self):
        max = self.__items[1]
        self.troca(1, self.__N)
        self.__N -= 1
        self.sink(1)
        self.__items[self.__N + 1] = None
        return max

    def menor(self, i, j):
        i = int(i)
        j = int(j)
        if self.__items[i] < self.__items[j]:
            return True
        else:
            return False

    def troca(self, i, j):
        i = int(i)
        j = int(j)
        temp = self.__items[i]
        self.__items[i] = self.__items[j]
        self.__items[j] = temp

    def print(self):
        print(self.__items)

    def __print(self, k, depth):

        if k >= len(self.__items) or self.__items[k] == None:
            print("---" * depth, "*")
            return

        print("\t")
        print("---" * depth, self.__items[k])

        self.__print(2*k, depth +1)
        self.__print(2*k+1, depth +1)

    def printTree(self):
        self.__print(1, 0)
