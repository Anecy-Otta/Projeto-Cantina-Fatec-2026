import pickle
import os
import random
from faker import Faker
from models import Produto

fake = Faker('pt_BR')

def salvar(dados, caminho_arquivo):
    """Garante que a pasta exista e salva os dados em um arquivo .pkl"""
    pasta = os.path.dirname(caminho_arquivo)
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)
    
    try:
        with open(caminho_arquivo, 'wb') as f:
            pickle.dump(dados, f)
        print(f">> Dados gravados em '{caminho_arquivo}'")
    except Exception as e:
        print(f">> Erro ao salvar arquivo: {e}")

def carregar(arquivo):
    """Lê os dados do arquivo .pkl. Retorna None se o arquivo não existir."""
    if not os.path.exists(arquivo):
        return None
    try:
        with open(arquivo, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        print(f">> Erro ao carregar arquivo: {e}")
        return None

def gerar_massa_dados(qtd=5):
    """Gera uma lista de lanches reais para a Cantina"""
    cardapio = [
        "Coxinha de Frango", "Pão de Queijo", "Misto Quente", 
        "Salgado Assado", "Suco Natural", "Refrigerante Lata", 
        "Bolo de Pote", "Café Expresso", "Sanduíche Natural", "Esfiha Carne"
    ]
    
    produtos_fakes = []
    for _ in range(qtd):
        nome_sorteado = random.choice(cardapio)
        p_compra = round(random.uniform(2.50, 5.00), 2)
        p_venda = round(p_compra * 1.6, 2) # Margem de lucro de 60%
        
        p = Produto(
            nome=nome_sorteado,
            preco_compra=p_compra,
            preco_venda=p_venda,
            data_compra="2026-03-26",
            data_validade="2026-04-10",
            quantidade=random.randint(5, 30)
        )
        produtos_fakes.append(p)
        
    return produtos_fakes
