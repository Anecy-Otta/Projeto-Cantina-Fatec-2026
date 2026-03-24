class EstoqueService:
    def __init__(self, fila):
        self.fila = fila

    def adicionar_produto(self, produto):
        self.fila.enqueue(produto)

    def baixar_estoque(self, quantidade):
        while quantidade > 0:
            produto = self.fila.itens[0]

            if produto.quantidade <= quantidade:
                quantidade -= produto.quantidade
                self.fila.dequeue()
            else:
                produto.quantidade -= quantidade
                quantidade = 0

class VendaService:
    def __init__(self, estoque, pagamentos, consumos):
        self.estoque = estoque
        self.pagamentos = pagamentos
        self.consumos = consumos

    def realizar_venda(self, nome_cliente, categoria, curso, produto_nome, quantidade):
        produto = self.estoque.fila.itens[0]

        valor_total = produto.preco_venda * quantidade

        pagamento = Pagamento(nome_cliente, categoria, curso, valor_total, "agora")
        self.pagamentos.adicionar(pagamento)

        self.estoque.baixar_estoque(quantidade)

        consumo = Consumo(produto_nome, quantidade, pagamento)
        self.consumos.adicionar(consumo)
