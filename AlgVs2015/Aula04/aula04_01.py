from aula04_queue import *

# Exemplo de uso de fila
listaDeExemplo = ["primeiro","segundo","terceiro","quarto","quinto"]

linkedListQueue = LinkedListQueue()

for word in listaDeExemplo:
    linkedListQueue.enqueue(word)

for word in listaDeExemplo:
    print(linkedListQueue.dequeue())

# output: primeiro, segundo, terceiro, quarto, quinto

arrayQueue = ArrayQueue(5)

for word in listaDeExemplo:
    arrayQueue.enqueue(word)

for word in listaDeExemplo:
    print(arrayQueue.dequeue())

arrayQueue.enqueue("sexto")
print(arrayQueue.dequeue())
arrayQueue.enqueue("setimo")
arrayQueue.enqueue("oitavo")
print(arrayQueue.dequeue())
