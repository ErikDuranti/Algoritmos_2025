from Pessoa import Pessoa
from Produto import Produto
from Pedido import Pedido
from Cidade import Cidade

c1 = Cidade()
c2 = Cidade("João Pessoa")

p1 = Pessoa("Fulano")
p2 = Pessoa("Ciclano", cid=c1)

prod01 = Produto("Coca-cola", 9.99)
prod02 = Produto("Pepsi", qtd=10)
prod03 = Produto("Fanta", 17.85, 30)

ped = Pedido(cliente=p2)
ped.addProd(prod02)
ped.addProd(prod03)

print(ped)