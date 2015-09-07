# =============================================================================================
# Classe <int>
# =============================================================================================
# Números inteiros de magnitude arbitrária
# =============================================================================================
x = 100
print(x)
print(type(x))

x = int("-100") # Parse de string
print("valor {0} e tipo {1}".format(x, type(x)))

x = int(5600.50) # Parse de float
print("valor {0} e tipo {1}".format(x, type(x)))

print("valor {0} e bits usados {1}".format(x, x.bit_length())) # bit_length: total de bits utilizados para armazenar o valor

x = int("010", 2) # Criação de inteiro com base 2
print("valor {0} e tipo {1}".format(x, type(x)))

x = int(1000000000000000000000000000) # Criação de inteiro positivo com grande magnitude
print("valor {0} e tipo {1}".format(x, type(x)))

x = int(-1000000000000000000000000000) # Criação de inteiro negativo com grande magnitude
print("valor {0} e tipo {1}".format(x, type(x)))