# =============================================================================================
# Classe <list>
# =============================================================================================
# Lista mutável de valores indexados, não necessariamente do mesmo tipo
# =============================================================================================

# Define uma lista vazia
x = [] 
print(len(x))
print(type(x))

# Define uma lista com elementos de tipos distintos
x = [1,2,3,4,'a']
print(x)

# Acesso a um item da lista (índice começa em 0)
print(x[4])

# Modifica um item da lista
x[4] = 'b'
print(x[4])

# Copia uma lista
y = x[:] # equivalente a x[0:4]
y[4] = 'c'
print(y)
print(x)

# Fatiamento de lista
print(x[0:2])
print(x[-1]) # Índice negativo acessa a lista de trás para frente

# Inclusão de item no final da lista
x.append("ultimo")
print(x)

# Inclusão de item em uma posição específica
x.insert(1, "segundo")
print(x)

# Adição de listas
x = [1,2,3]
y = [3,4,5]
x = x + y
print(x)

# Remoção de item da lista
del(x[3])
print(x)

# Retornar o valor do item na posição e excluí-lo da lista
y = x.pop(0) # Se Nenhum índice for informado, retornará o último item
print(y)
print(x)

# Percorrendo todos os items da lista
for i in x:
    print(i)

# Transformando o resultado de um range numa lista
x = list(range(0,10))
print(x)

# Uso de enumerate para acessar valor e índice do item
x = ['a', 'b', 'c']
for i,v in enumerate(x):
    print("i={0}, v={1}".format(i,v))
