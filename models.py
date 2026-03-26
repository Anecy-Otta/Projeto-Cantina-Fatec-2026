import datetime

class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_validade, quantidade):
        self._nome = nome
        self._preco_compra = preco_compra
        self._preco_venda = preco_venda
        self._data_compra = data_compra
        self._data_validade = data_validade
        self._quantidade = quantidade

    @property
    def nome(self):
        return self._nome

    @property
    def preco_venda(self):
        return self._preco_venda

    @preco_venda.setter
    def preco_venda(self, valor):
        if valor >= self._preco_compra:
            self._preco_venda = valor
        else:
            raise ValueError("O preço de venda não pode ser menor que o preço de compra.")

    @property
    def quantidade(self):
        return self._quantidade

    def atualizar_estoque(self, valor):
        if self._quantidade + valor >= 0:
            self._quantidade += valor
        else:
            raise ValueError("Estoque insuficiente.")

class Pagamento:
    def __init__(self, nome, categoria, curso, valor, data_hora=None):
        self._nome = nome
        self._categoria = categoria
        self._curso = curso
        self._valor = valor
        self._data_hora = data_hora or datetime.datetime.now()

    @property
    def valor(self):
        return self._valor

class Consumo:
    def __init__(self, produto, quantidade, pagamento):
        self._produto = produto
        self._quantidade = quantidade
        self._pagamento = pagamento
