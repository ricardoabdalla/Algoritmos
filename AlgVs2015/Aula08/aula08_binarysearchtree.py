from math import floor
from aula08_node import Node
from aula08_key import Key

class BinarySearchTree(object):
    """Implementação de Binary Search Tree"""

    __root = None

    def put(self, key, value):
        self.__root = self.__put(self.__root, Key(key), value)

    def __put(self, node, key, value):

        if node == None:
            return Node(key, value)

        result = key.compareTo(node.key)

        if result < 0:
            node.left = self.__put(node.left, key, value)
        elif result > 0:
            node.right = self.__put(node.right, key, value)
        else: 
            node.value = value

        node.count = 1 + self.__size(node.left) + self.__size(node.right);
        
        return node

    def get(self, key):

        if not isinstance(key, Key):
            key = Key(key)

        currentNode = self.__root

        while currentNode != None:
            result = key.compareTo(currentNode.key)
            if result < 0:
                currentNode = currentNode.left
            elif result > 0:
                currentNode = currentNode.right
            else: 
                return currentNode.value

        return None

    def floor(self, key):
        if not isinstance(key, Key):
            key = Key(key)

        x = self.__floor(self.__root, key)
        if x == None:
            return None
        return x.key

    def __floor(self, node, key):

        if node == None:
            return None

        result = key.compareTo(node.key)

        if result == 0:
            return node
        elif result < 0:
            return self.__floor(node.left, key)

        t = self.__floor(node.right, key)

        if t != None:
            return t;
        else:
            return node

    def size(self):
        return self.__size(self.__root)

    def __size(self, node):
        if node == None:
            return 0
        return node.count

    def isEmpty(self):
        return self.size() == 0

    def min(self):
        if self.isEmpty(): 
            raise ValueError("min() foi chamado com arvore vazia")
        return self.__min(self.__root).key

    def __min(self, node):
        if node.left == None:
            return node
        else:
            return self.__min(node.left)

    def delete(self, key):
        raise NotImplementedError
