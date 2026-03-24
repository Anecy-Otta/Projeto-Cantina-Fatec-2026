class Produto:
    def __init__(self, nome, preco_compra, preco_venda, data_compra, data_validade, quantidade):
        self.nome = nome
        self.preco_compra = preco_compra
        self.preco_venda = preco_venda
        self.data_compra = data_compra
        self.data_validade = data_validade
        self.quantidade = quantidade

class Pagamento:
    def __init__(self, nome, categoria, curso, valor, data_hora):
        self.nome = nome
        self.categoria = categoria
        self.curso = curso
        self.valor = valor
        self.data_hora = data_hora

class Consumo:
    def __init__(self, produto, quantidade, pagamento):
        self.produto = produto
        self.quantidade = quantidade
        self.pagamento = pagamento
