import os
from models import Produto
from estrutura import FilaEstoque, ListaPagamentos, ListaConsumo
from services import EstoqueService, VendaService
from utils import salvar, carregar, gerar_massa_dados

PATH_ESTOQUE = 'data/estoque.pkl'
PATH_VENDAS = 'data/vendas.pkl'
PATH_CONSUMO = 'data/consumo.pkl'

def exibir_menu():
    print("\n" + "—"*35)
    print("   CANTINA FATEC 2026 - TERMINAL")
    print("—"*35)
    print("1. Cadastrar Produto (Lote)")
    print("2. Gerar Dados Fakes (Testes)")
    print("3. Visualizar Estoque")
    print("4. Realizar Venda")
    print("5. Relatório de Vendas")
    print("0. Salvar e Sair")
    return input("\nEscolha uma opção: ")

def main():
    fila_estoque = FilaEstoque()
    lista_pagamentos = ListaPagamentos()
    lista_consumo = ListaConsumo()

    print(">> Carregando dados...")
    dados_e = carregar(PATH_ESTOQUE)
    if dados_e:
        for p in dados_e: fila_estoque.enqueue(p)
    
    dados_v = carregar(PATH_VENDAS)
    if dados_v:
        for v in dados_v: lista_pagamentos.adicionar(v)

    estoque_service = EstoqueService(fila_estoque)
    venda_service = VendaService(estoque_service, lista_pagamentos, lista_consumo)

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            try:
                nome = input("Nome do Produto: ")
                p_compra = float(input("Preço de Compra: "))
                p_venda = float(input("Preço de Venda: "))
                qtd = int(input("Quantidade: "))
                novo_p = Produto(nome, p_compra, p_venda, "2026-03-26", "2026-12-31", qtd)
                estoque_service.adicionar_produto(novo_p)
                print(f" {nome} adicionado ao estoque.")
            except Exception as e:
                print(f" Erro: {e}")

        elif opcao == "2":
            fakes = gerar_massa_dados(5)
            for p in fakes: estoque_service.adicionar_produto(p)
            print(" 5 produtos fakes injetados no sistema.")

        elif opcao == "3":
            print("\n--- STATUS DO ESTOQUE ---")
            itens = fila_estoque.listar_produtos()
            if not itens:
                print("Estoque vazio!")
            for p in itens:
                print(f" {p.nome} | Qtd: {p.quantidade} | Preço: R${p.preco_venda:.2f}")

        elif opcao == "4":
            try:
                cliente = input("Nome do Aluno: ")
                curso = input("Curso: ")
                prod_nome = input("O que ele comprou?: ")
                qtd_venda = int(input("Quantidade: "))
                
                total = venda_service.realizar_venda(cliente, "Lanche", curso, prod_nome, qtd_venda)
                print(f" Venda realizada! Total: R${total:.2f}")
            except Exception as e:
                print(f" Erro na venda: {e}")

        elif opcao == "5":
            print("\n--- RESUMO FINANCEIRO ---")
            total_arrecadado = sum(p.valor for p in lista_pagamentos.pagamentos)
            print(f"Faturamento Total: R$ {total_arrecadado:.2f}")
            print(f"Total de pedidos: {len(lista_pagamentos.pagamentos)}")

        elif opcao == "0":
            # Salva antes de encerrar
            salvar(fila_estoque.listar_produtos(), PATH_ESTOQUE)
            salvar(lista_pagamentos.pagamentos, PATH_VENDAS)
            print(" Dados salvos com sucesso. Encerrando...")
            break

if __name__ == "__main__":
    main()
