class FilaEstoque:
    def __init__(self):
        self.__itens = [] 

    def enqueue(self, produto):
        if isinstance(produto, Produto):
            self.__itens.append(produto)
        else:
            raise TypeError("Apenas objetos da classe Produto podem ser adicionados.")

    def dequeue(self):
        if not self.is_empty():
            return self.__itens.pop(0)
        return None

    def is_empty(self):
        return len(self.__itens) == 0

    def listar_produtos(self):
        return list(self.__itens) 

class ListaPagamentos:
    def __init__(self):
        self._pagamentos = []

    def adicionar(self, pagamento):
        self._pagamentos.append(pagamento)

class ListaConsumo:
    def __init__(self):
        self._consumos = []

    def adicionar(self, consumo):
        self._consumos.append(consumo)
