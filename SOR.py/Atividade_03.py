
class Carro:
    consumo = 0
    tanque = 0.0

    def __init__(self, consumo):
         self.consumo = consumo
     
    def andar(self, distancia):
        print(f"Você andou {distancia} km")
        self.tanque -= distancia/self.consumo

    def obterGas(self):
        print(f"Você tem {str(self.tanque).replace('.', ',')} litros de gasolina no tanque")

    def porGas(self, combustivel):
        print(f"Você abasteceu {combustivel} litros de gasolina")
        self.tanque += combustivel

x = int(input("Qual o consumo do seu carro?: "))
y = Carro(x)
b = int(input("Quanto você quer pôr de gasolina?: "))
y.porGas(b)
c = int(input("Quantos km você percorreu?: "))
y.andar(c)
y.obterGas()

