class Key(object):
    """Implementação de Key para Nó de Binary Search Tree"""
    __key = None

    def __init__(self, key):
        if key == None or key == "":
            raise ValueError("key não pode ser nulo ou vazio")

        self.__key = key

    def compareTo(self, obj):

        if self.__key == obj.__key:
            return 0
        elif self.__key < obj.__key:
            return -1
        else:
            return 1