from aula08_key import Key

class Node(object):
    """Implementação de Nó para Binary Search Tree"""
    key = None
    value = None
    left = None
    right = None

    def __init__(self, key, value):

        if key == None or not isinstance(key, Key):
            raise ValueError("key é nulo ou possui tipo inválido")

        self.key = key
        self.value = value

    #def key(self):
    #    return self.__key
        