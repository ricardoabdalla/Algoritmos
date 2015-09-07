# =============================================================================================
# Classe <list>
# =============================================================================================
# Lista mutável de valores, não necessariamente do mesmo tipo
# =============================================================================================

# Define uma lista mutável
listaDeNumeros = [1,2,3,4,5] 

# For (iteração em coleção)
for num in listaDeNumeros:
    print(num)

# For baseado em índice
# range(n): gera uma série de números de 0 a n-1 
for j in range(len(listaDeNumeros)): 
    print("j = {0}, valor = {1}".format(j, listaDeNumeros[j]))

# Range de números de 0 até 19, com incremento de 2 
for k in range(0, 20, 2): 
    print("k = {0}".format(k))

