# =============================================================================================
# Classes
# =============================================================================================

class Salario(object):
    """Representa o tipo Salario"""

    # Membro privado para armazenar o valor do salário
    __valor = 0.0

    # Método construtor
    def __init__(self, v):
        if v < 0:
            raise ValueError("Salário não pode ser negativo")
        self.__valor = v

    # Método Set
    def aumentar(self, percentual):
        if percentual < 0 or percentual is None:
            raise Exception("Valor inválido")

        self.__valor = self.__valor * (1 + percentual)

    # Método Get
    def getSalario(self):
        return self.__valor


# Criando uma instância da classe
salario = Salario(1000.0)
print(salario.getSalario())

# Invocando método
salario.aumentar(0.10)
print(salario.getSalario())