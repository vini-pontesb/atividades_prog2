class CarrinhoDeCompras:
    def __init__(self):
        self.lista = []
    
    def adicionar_produtos(self, produto):
        self.lista.append(produto)
    
    def listar_produto(self):
        print(self.lista)

class Produto():
    def __init__(self,nome):
        self.nome = nome

produto1 = ("Macarrão")
produto2 = ("Linguiça")
produto3 = ("Molho")

carrinho = CarrinhoDeCompras()
carrinho.adicionar_produtos(produto1)
carrinho.adicionar_produtos(produto2)
carrinho.adicionar_produtos(produto3)
carrinho.listar_produto()