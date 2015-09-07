# =============================================================================================
# Classe <str> 
# =============================================================================================
# Cadeias de caracteres imutáveis
# =============================================================================================

# String definida com aspas simples
x = 'aspas simples' 
print(x)
print(type(x))

# String definida com aspas duplas
x = "aspas duplas"
print(x)
print(type(x))

x = "aspas duplas" # Literal definida com aspas duplas
# String definida com aspas triplas
x = '''\nExemplo de texto com 
múltiplas linhas\n'''
print(x)

x = "valor"

# Retorna o caractere na posição 0
print(x[0]) 

# Retorna 5 caracteres a partir da posição 0
print(x[0:5]) 

# Percorrendo os caracteres de uma string
for letra in x:
    print(letra)

# Retorna a cópia da sequência
print(x[:]) 

# Retorna o tamanho (length) da string
print(len(x)) 

# Retorna o número de ocorrências do caractere 'a'
print(x.count("a")) 

# Substitui ocorrências do caractere 'v' por 'c'
print(x.replace("v", "c"))

# Pesquisa a ocorrência de uma substring no texto. Retorna o índice de início ou -1 se não localizar
print(x.find("or")) 

# Remoção de espaços em branco
x = "      valor"
print(x.strip())

# Quebra de uma string a partir de um caractere informado
x = "1;2;3;4;5;a"
print(x.split(";"))