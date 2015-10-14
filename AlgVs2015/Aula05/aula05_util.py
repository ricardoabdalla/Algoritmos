def troca(colecao, i, j):
    temp = colecao[i]
    print("{0} <-> {1}".format(colecao[i], colecao[j]))
    colecao[i] = colecao[j]
    colecao[j] = temp
    print(colecao)    
    input()

def menor(x, y):
    if x < y:
        return True
    else:
        return False