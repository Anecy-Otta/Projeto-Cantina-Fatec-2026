class FilaEstoque:
    def __init__(self):
        self.itens = []

    def enqueue(self, produto):
        self.itens.append(produto)

    def dequeue(self):
        if not self.is_empty():
            return self.itens.pop(0)

    def is_empty(self):
        return len(self.itens) == 0
    
class ListaPagamentos:
    def __init__(self):
        self.pagamentos = []

    def adicionar(self, pagamento):
        self.pagamentos.append(pagamento)

class ListaConsumo:
    def __init__(self):
        self.consumos = []

    def adicionar(self, consumo):
        self.consumos.append(consumo)
