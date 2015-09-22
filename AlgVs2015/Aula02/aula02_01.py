from aula02_00 import *
from aula02_quickfind import *

# loadUfData(None, readUfData("data-uf.txt"))

quickFind = QuickFindUF(10)
quickFind.union(4, 3)
quickFind.union(3, 8)
quickFind.union(6, 5)
quickFind.union(9, 4)
quickFind.union(2, 1)
quickFind.print()
quickFind.connected(4, 3)
quickFind.connected(0, 9)
quickFind.connected(5, 6)