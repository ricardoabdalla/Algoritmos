from aula03_00 import *
from aula03_3sum import *
from time import time

x = ThreeSum()

a = readInts("100ints.txt")

startTime = time()
x.count(a)
endTime = time()
print("Tempo Gasto: = {0}".format(endTime - startTime))

a = readInts("200ints.txt")

startTime = time()
x.count(a)
endTime = time()
print("Tempo Gasto: = {0}".format(endTime - startTime))

a = readInts("300ints.txt")

startTime = time()
x.count(a)
endTime = time()
print("Tempo Gasto: = {0}".format(endTime - startTime))

a = readInts("400ints.txt")

startTime = time()
x.count(a)
endTime = time()
print("Tempo Gasto: = {0}".format(endTime - startTime))

a = readInts("500ints.txt")

startTime = time()
x.count(a)
endTime = time()
print("Tempo Gasto: = {0}".format(endTime - startTime))
