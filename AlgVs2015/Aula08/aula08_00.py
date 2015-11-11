from aula08_binarysearchtree import *

x = BinarySearchTree()
x.put(5, "cinco")
x.put(20, "vinte")
x.put(6, "seis")
x.put(3, "três")
x.put(1, "um")
print("Tamanho da BST: {0} no(s)".format(x.size()))
print("Menor chave: {0}".format(x.min().key))
print("Valor na chave {0}: {1}".format(6, x.get(6)))
print("Piso para chave {0}: {1}".format(2, x.floor(2).key))

x.deleteMin()
print("Tamanho da BST: {0} no(s)".format(x.size()))
print("Menor chave: {0}".format(x.min().key))

x.put(100, "cem")
print("Tamanho da BST: {0} no(s)".format(x.size()))
x.delete(100)
print("Tamanho da BST: {0} no(s)".format(x.size()))

x.put(1, "um")
x.put(21, "vinte e um")
x.put(4, "quatro")
x.printTree()