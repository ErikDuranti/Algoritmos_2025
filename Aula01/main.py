class Carro:
    def __init__(self, modelo, ano, km):
        self.modelo = modelo;
        self.ano = ano;
        self.km = km;
    
    def inc_km(self, incremento):
        self.km = self.km + incremento
        
    
    def __str__(self):
        txt = "--------------------"
        txt += "\nModelo: " + self.modelo
        txt += "\nAno: " + self.ano
        txt += "\nKM Rodado: " + str(self.km)
        return txt
    
carro = Carro("HB20", "2025", 50)
carro.inc_km(100)
print (carro)