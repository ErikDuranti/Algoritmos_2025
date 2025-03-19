class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.kilometragem = 0
        
    def km(self):
        if km > 0:
            self.__kilometragem += km
        
    
    def setKM(self, km):
        if km > self._kilometragem:
            self.__kilometragem = km
            
    def __str__(self):
        txt = "Modelo: " + self.modelo
        txt += "\nAno: " + self.ano
        txt += "\nKilometragem: " + str(self.__kilometragem)
        return txt
            
x = Carrp("Doblo", 2025)
print (x)