class Pagamento:
    def pagar(self, valor):
        print(f"Pagando R${valor}")

class PagamentoPromessa(Pagamento):
    pass

class PagamentoCartao(Pagamento):
    def pagar(self, valor):
        print(f"Pagando no cartão R${valor}")

class PagamentoPix(Pagamento):
    def pagar(self, valor):
        print(f"Pagando no PIX R${valor}")

# Polimorfismo:
# A função recebe qualquer objeto que seja um Pagamento
# (ou herde de Pagamento) e chama o método pagar().
# Não importa qual classe implementou o método.
def realizar_pagamento(meio: Pagamento, valor):
    meio.pagar(valor)


promessa = PagamentoPromessa()
cartao = PagamentoCartao()
pix = PagamentoPix()

realizar_pagamento(cartao, 150)
realizar_pagamento(pix, 150)
realizar_pagamento(promessa, 150)
