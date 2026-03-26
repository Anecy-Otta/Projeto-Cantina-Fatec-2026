import pickle
import os 
import random
from faker import Faker
from models import Produto

fake = Faker('pt_BR')

def salvar(dados, caminho_arquivo):
    pasta = os.path.dirname(caminho_arquivo)
    
    if pasta and not os.path.exists(pasta):
        os.makedirs(pasta)
        print(f">> Pasta '{pasta}' criada com sucesso.")

    try:
        with open(caminho_arquivo, 'wb') as f:
            pickle.dump(dados, f)
        print(f">> Arquivo '{caminho_arquivo}' gravado com sucesso!")
    except Exception as e:
        print(f">> Erro ao gravar arquivo: {e}")

def carregar(arquivo):
    if not os.path.exists(arquivo):
        return None
    try:
        with open(arquivo, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        print(f">> Erro ao carregar: {e}")
        return None

def gerar_massa_dados(qtd=5):
    produtos_fakes = []
    for _ in range(qtd):
        p = Produto(
            nome=fake.word().capitalize(),
            preco_compra=round(random.uniform(2.0, 5.0), 2),
            preco_venda=round(random.uniform(6.0, 12.0), 2),
            data_compra="2026-03-26",
            data_validade="2026-12-31",
            quantidade=random.randint(10, 50)
        )
        produtos_fakes.append(p)
    return produtos_fakes
