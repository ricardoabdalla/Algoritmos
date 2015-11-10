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

    def delete(self, key):
        raise NotImplementedError
