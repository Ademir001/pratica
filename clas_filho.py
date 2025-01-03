class Produto:  # Corrigido para seguir a convenção de nomes (letra maiúscula para classes)
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    # Getter para o preço
    def get_preco(self):
        return self.__valor

    # Setter para o preço
    def set_preco(self, valor):
        if valor > 0:
            self.__valor = valor
        else:
            print("Preço inválido")  # Corrigido para português claro

# Lista de produtos
p = [
    Produto("Celular", 1500), 
    Produto("Saco de sal", 2334)  # Corrigido o nome
]

for i in p:
    print(f"produto: {i.get_preco()}")