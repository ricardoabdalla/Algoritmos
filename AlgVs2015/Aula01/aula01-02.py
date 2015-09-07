# =============================================================================================
# Classe <float> 
# =============================================================================================
# Números com ponto flutuante: max=1.7976931348623157e+308 min=2.2250738585072014e-308
# =============================================================================================
x = 5600.50
print(x)
print(type(x))

x = float("100.5") # Parse de string para número positivo
print("valor {0} e tipo {1}".format(x, type(x)))

x = float("-100.5") # Parse de string para número negativo
print("valor {0} e tipo {1}".format(x, type(x)))

x = float(-100.5)
print("valor {0} e tipo {1}".format(x, type(x)))

x = float("32.3e5")
print("valor {0:.2f} e tipo {1}".format(x, type(x)))

x = float("32.3e-5")
print("valor {0:.6f} e tipo {1}".format(x, type(x)))