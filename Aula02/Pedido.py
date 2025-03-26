from Pessoa import Pessoa
from Cidade import Cidade
from Produto import Produto

class Pedido:
    def __init__(self, data, cliente = Pessoa("Fulano")):
        self.id = None
        self.data = data
        self.cliente = cliente
        self.produtos = []
        
    def addProd(self, prod):
        if prod != None and prod.preco > 10.0:
            self.produtos.append(prod)
        soma = 0.0
        for p in self.produtos:
            soma += p.preco
        return soma
    
    def __str__(self):
        txt = "Pedido realizado em: " + str(self.data)
        # txt += "\nCliente: " + str(self.cliente)
        txt += "\nCliente: " + str(self.cliente)
        txt += "\nProdutos: "
        for p in self.produtos:
            txt += "\n" + str(p)
            txt += "-------------------------------------"
        txt += "\nPedido: " + str(self.id)