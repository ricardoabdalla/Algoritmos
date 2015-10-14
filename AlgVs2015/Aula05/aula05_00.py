from aula05_selectionsort import *
from aula05_insertionsort import *
from aula05_shellsort import *


colecaoModelo = [4, 6, 8, 1, 9, 3, 2, 0, 5, 7] # n = 10

#c1 = colecaoModelo[:]
#print(c1)

#print("Selection Sort")
#selectionSort = Selection()
#selectionSort.sort(c1)

#print(c1)

#c2 = colecaoModelo[:]
#print(c2)

#print("Insertion Sort")
#insertionSort = Insertion()
#insertionSort.sort(c2)

#print(c2)

c3 = colecaoModelo[:]
print(c3)

print("Shell Sort")
shellSort = Shell()
shellSort.sort(c3)

print(c3)