import datetime
from models import Pagamento, Consumo

class EstoqueService:
    def __init__(self, fila_estoque):
        self.fila = fila_estoque

    def adicionar_produto(self, produto):
        self.fila.enqueue(produto)

    def baixar_estoque(self, quantidade_total):
        while quantidade_total > 0 and not self.fila.is_empty():
            produtos_no_estoque = self.fila.listar_produtos()
            produto_atual = produtos_no_estoque[0] 

            if produto_atual.quantidade <= quantidade_total:
                quantidade_total -= produto_atual.quantidade
                self.fila.dequeue()
            else:
                produto_atual.atualizar_estoque(-quantidade_total)
                quantidade_total = 0

class VendaService:
    def __init__(self, estoque_service, lista_pagamentos, lista_consumo):
        self.estoque_service = estoque_service
        self.pagamentos = lista_pagamentos
        self.consumos = lista_consumo

    def realizar_venda(self, nome_cliente, categoria, curso, produto_nome, quantidade):
        itens = self.estoque_service.fila.listar_produtos()
        if not itens:
            raise ValueError("Não há produtos no estoque!")
        
        produto_referencia = itens[0]
        valor_total = produto_referencia.preco_venda * quantidade

        pagamento = Pagamento(nome_cliente, categoria, curso, valor_total, datetime.datetime.now())
        self.pagamentos.adicionar(pagamento)

        self.estoque_service.baixar_estoque(quantidade)

        consumo = Consumo(produto_nome, quantidade, pagamento)
        self.consumos.adicionar(consumo)
        
        return valor_total
    


if __name__ == "__main__":
    print("--- Testando os Serviços ---")
    print("Serviços carregados com sucesso!")
