class Rama:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None
class Arvore_binaria:
    def __init__(self):
        self.raiz = None
    def ordem(self, rama):
        if rama:
            self.ordem(rama.esquerda)
            print(rama.valor, end="")
            self.ordem(rama.direira)
ar = Arvore_binaria()
ar.raiz = Rama(10)
ar.raiz.esquerda = Rama(5)
ar.raiz.direita = Rama(15)

ar.ordem(ar.raiz)