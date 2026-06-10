#crio uma interface que qualquer pagamento tenha o metodo pagar ABC = abstrct base class
from abc import ABC, abstractmethod
#aqui esta o "molde"
class Pagamento:
    @abstractmethod
    def pagar(self, valor):
        pass

class PagamentoPromessa(Pagamento):
    def pagar(self, valor):
        print(f"Pagando na promessa R${valor}")

class PagamentoCartao(Pagamento):
    def pagar(self, valor):
        print(f"Pagando no cartão R${valor}")

class PagamentoPix(Pagamento):
    def pagar(self, valor):
        print(f"Pagando no PIX R${valor}")
        
class PagamentoBoleto(Pagamento):
    def pagar(self, valor):
        print(f"Pagando no boleto R${valor}")


def realizar_pagamento(meio: Pagamento, valor):
    meio.pagar(valor)


promessa = PagamentoPromessa()
cartao = PagamentoCartao()
pix = PagamentoPix()

realizar_pagamento(cartao, 150)
realizar_pagamento(pix, 150)
realizar_pagamento(promessa, 150)
