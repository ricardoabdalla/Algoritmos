class Key(object):
    """Implementação de Key para Nó de Binary Search Tree"""
    key = None

    def __init__(self, key):
        if key == None or key == "":
            raise ValueError("key não pode ser nulo ou vazio")

        self.key = key

    def compareTo(self, obj):

        if self.key == obj.key:
            return 0
        elif self.key < obj.key:
            return -1
        else:
            return 1