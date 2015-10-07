from aula04_node import Node

class Stack(object):
    """Interface desejada para Stack"""

    def push(self, item):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def isEmpty(self):
        raise NotImplementedError


class LinkedListStack(object):
    """Implementação de Stack utilizando lista ligada"""

    __first = None

    # Adiciona item no topo da pilha
    def push(self, item):
        oldFirst = self.__first
        self.__first = Node()
        self.__first.item = item
        self.__first.next = oldFirst

    # Remove item do topo da pilha
    def pop(self):
        item = self.__first.item
        self.__first = self.__first.next
        return item

    # Indica se a pilha encontra-se vazia
    def isEmpty(self):
        return self.__first == None

class ArrayStack(object):
    """Implementação de Stack utilizando array de tamanho fixo"""

    __N = 0
    __items = []
    __capacity = 0

    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacidade não pode ser nula ou negativa")
        self.__capacity = capacity

        for i in range(self.__capacity):
            self.__items.append(None)

    def push(self, item):
        
        if self.__N >= self.__capacity:
            raise IndexError("Out of bound")
        self.__items[self.__N] = item
        self.__N += 1

    def pop(self):
        self.__N -= 1
        if self.__N < 0:
            raise IndexError("Out of bound")
        item = self.__items[self.__N]
        self.__items[self.__N] = None        
        return item

    def isEmpty(self):
        return self.__N == 0