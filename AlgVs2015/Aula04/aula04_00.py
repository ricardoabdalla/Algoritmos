from aula04_stack import *

# Exemplo de uso de pilha
listaDeExemplo = ["to","be","or","not","to","-","be","-","-","that","-","-","-","is"]

linkedListStack = LinkedListStack()

for word in listaDeExemplo:
    if word == "-":
        item = linkedListStack.pop()
        print(item)
    else:
        linkedListStack.push(word)

# output: to be not that or be

arrayStack = ArrayStack(5)
arrayStack.push("a")
arrayStack.push("b")
arrayStack.push("c")
arrayStack.push("d")
arrayStack.push("e")
print(arrayStack.pop())
arrayStack.push("f")
print(arrayStack.pop())

arrayStack = ArrayStack(10)

for word in listaDeExemplo:
    if word == "-":
        item = arrayStack.pop()
        print(item)
    else:
        arrayStack.push(word)