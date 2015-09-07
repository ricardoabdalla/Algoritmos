# =============================================================================================
# Classe <bool> 
# =============================================================================================
# Valores booleanos: True ou False
# =============================================================================================
x = True
print(x)
print(type(x))

x = False
print(x)
print(type(x))

x = bool(0) # 0 é o único número False
print("valor {0} e tipo {1}".format(x, type(x)))

x = bool(1)
print("valor {0} e tipo {1}".format(x, type(x)))

x = bool(-1)
print("valor {0} e tipo {1}".format(x, type(x)))

x = bool("") # string vazia retorna False
print("valor {0} e tipo {1}".format(x, type(x)))

x = bool("non-empty")
print("valor {0} e tipo {1}".format(x, type(x)))