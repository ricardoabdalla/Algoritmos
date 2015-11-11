from aula08_binarysearchtree import *

x = BinarySearchTree()
x.put(5, "cinco")
x.put(6, "seis")
x.put(3, "três")
x.put(1, "um")
print(x.size())
print(x.min().key)
print(x.get(6))
print(x.size())
print(x.floor(2).key)