# =============================================================================================
# Tratamento de Erros
# =============================================================================================

def divide(x,y):

    try:
        return x/y
    except ArithmeticError:
        print("Valores inválidos para divisão")
        return None
    else:
        print("Erro desconhecido")
        return None


print(divide(4,2))
print(divide(0,2))
print(divide(2,0))