from math import floor
from aula08_node import Node
from aula08_key import Key

class BinarySearchTree(object):
    """Implementação de Binary Search Tree"""

    __root = None

    """Adiciona chave/valor na árvore"""
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

    """Obtém o valor da chave informada"""
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

    """Obtém a maior chave menor ou igual a chave informada"""
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

    """Obtém o número de nós existente na BST"""
    def size(self):
        return self.__size(self.__root)

    def __size(self, node):
        if node == None:
            return 0
        return node.count

    def isEmpty(self):
        return self.size() == 0

    """Obtém a menor chave existente na BST"""
    def min(self):
        if self.isEmpty(): 
            raise ValueError("min() foi chamado com arvore vazia")
        return self.__min(self.__root).key

    def __min(self, node):
        if node.left == None:
            return node
        else:
            return self.__min(node.left)

    """Remove a menor chave existente na BST"""
    def deleteMin(self):
        self.__root = self.__deleteMin(self.__root)

    def __deleteMin(self, node):        
        if node.left == None:
            return node.right
        node.left = self.__deleteMin(node.left)
        node.count = 1 + self.__size(node.left) + self.__size(node.right)
        return node

    """Remove a chave informada da BST"""
    def delete(self, key):

        if not isinstance(key, Key):
            key = Key(key)

        self.__root = self.__delete(self.__root, key)

    def __delete(self, node, key):
        
        if node == None:
            return None

        result = key.compareTo(node.key)

        if result < 0:
            node.left = self.__delete(node.left, key)
        elif result > 0:
            node.right = self.__delete(node.right, key)
        else:
            if node.right == None:
                return node.left
            if node.left == None:
                return node.right

            t = node
            node = self.__min(t.right)
            node.right = self.__deleteMin(t.right)
            node.left = t.left

        node.count = 1 + self.__size(node.left) + self.__size(node.right)
        return node

    """Imprime na tela a configuração da BST"""
    def printTree (self):
        self.__printTree(self.__root, 0)

    def __printTree (self, node, depth):
        if node.left != None:
            self.__printTree(node.left, depth + 1)
        print("---" * depth, node.key.key)
        if node.right != None:
            self.__printTree(node.right, depth + 1)