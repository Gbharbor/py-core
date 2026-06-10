# Herança
class Animal:
    def fazer_som(self):
        print("Algum som")

class Cachorro(Animal):
    pass

dog = Cachorro()
dog.fazer_som()


# Composição
class Motor:
    def ligar(self):
        print("Ligando...")

class Carro:
    def __init__(self):
        self.motor = Motor()  # Carro possui um Motor

    def ligar(self):
        self.motor.ligar()

fiat = Carro()
fiat.ligar()
