from models import Produto

class FilaEstoque:
    def __init__(self):
        self.itens = [] 

    def enqueue(self, produto):
        if isinstance(produto, Produto):
            self.itens.append(produto)
        else:
            raise TypeError("O item deve ser um objeto da classe Produto")

    def dequeue(self):
        if not self.is_empty():
            return self.itens.pop(0)
        return None

    def is_empty(self):
        return len(self.itens) == 0

    def listar_produtos(self):
        return list(self.itens)

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
