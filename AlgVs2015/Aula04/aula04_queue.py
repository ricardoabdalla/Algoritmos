from aula04_node import Node

class Queue(object):
    """Interface desejada para Queue"""

    def enqueue(self, item):
        raise NotImplementedError

    def dequeue(self):
        raise NotImplementedError

    def isEmpty(self):
        raise NotImplementedError


class LinkedListQueue(object):
    """Implementação de Queue utilizando lista ligada"""

    __first = None
    __last = None

    # Adiciona item no início da fila
    def enqueue(self, item):
        oldLast = self.__last
        self.__last = Node()
        self.__last.item = item
        self.__last.next = None
        if self.isEmpty():
            self.__first = self.__last
        else:
            oldLast.next = self.__last

    # Remove item do final da fila
    def dequeue(self):
        item = self.__first.item
        self.__first = self.__first.next
        if self.isEmpty():
            self.__last = None
        return item

    # Indica se a fila encontra-se vazia
    def isEmpty(self):
        return self.__first == None

class ArrayQueue(object):
    """Implementação de Queue utilizando array de tamanho fixo"""

    __N = 0 # Numero de elementos na fila
    __items = []
    __capacity = 0
    __first = 0 # Índice do primeiro elemento da fila
    __last = 0 # Índice do próximo slot disponível

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacidade não pode ser nula ou negativa")
        self.__capacity = capacity

        for i in range(self.__capacity):
            self.__items.append(None)

    def enqueue(self, item):
        
        if self.__N >= self.__capacity:
            raise IndexError("Out of bound")
        self.__items[self.__last] = item
        self.__last += 1
        if self.__last == len(self.__items):
            self.__last = 0
        self.__N += 1

    def dequeue(self):
        self.__N -= 1
        if self.__N < 0:
            raise IndexError("Out of bound")
        item = self.__items[self.__first]
        self.__items[self.__first] = None 
        self.__first += 1
        if self.__first == len(self.__items):
            self.__first = 0       
        return item

    def isEmpty(self):
        return self.__N == 0