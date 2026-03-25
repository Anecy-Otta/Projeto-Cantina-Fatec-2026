import pickle

def salvar(dados, arquivo):
    with open(arquivo, 'wb') as f:
        pickle.dump(dados, f)

def carregar(arquivo):
    with open(arquivo, 'rb') as f:
        return pickle.load(f)
    
def relatorio_vendas(lista_pagamentos):
    total = 0
    for p in lista_pagamentos.pagamentos:
        total += p.valor
    return total

def relatorio_consumo(lista_consumo):
    for c in lista_consumo.consumos:
        print(c.produto, c.quantidade)
