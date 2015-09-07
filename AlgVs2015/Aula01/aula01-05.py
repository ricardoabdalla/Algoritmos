# =============================================================================================
# Controle de Fluxo
# =============================================================================================
# if <condicao>:
#     bloco verdadeiro
# elif <condicao>:
#     bloco verdadeiro
# else:
#     bloco falso
# =============================================================================================

# String definida com aspas simples
x = int(input("Informe um numero inteiro de 0 a 100:"))

# Condicional: If...Elif...Else
if x > 80:
    print("Valor maior do que 80")
elif x <= 80 and x > 0:
    print("Valor menor ou igual do que 80 e positivo")
elif x == 0:
    print("Valor é zero")
else:
    print("Valor é negativo")

# If aninhado
if x > 80:
    print("Valor maior do que 80")
    if x % 2 == 0:
        print("Valor é par")
    else:
        print("Valor é ímpar")

# OBS: Python não possui switch