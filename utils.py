import pickle
import random
from faker import Faker
from models import Produto, Pagamento

fake = Faker('pt_BR')

def salvar(dados, arquivo):
    """Salva qualquer objeto em um arquivo binário."""
    with open(arquivo, 'wb') as f:
        pickle.dump(dados, f)

def carregar(arquivo):
    """Carrega dados de um arquivo binário. Retorna None se o arquivo não existir."""
    try:
        with open(arquivo, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return None

def gerar_massa_dados(qtd_produtos=5):
    """Gera uma lista de produtos fakes para popular o sistema."""
    produtos_fakes = []
    for _ in range(qtd_produtos):
        p_compra = round(random.uniform(1.0, 5.0), 2)
        p_venda = round(p_compra * 1.8, 2)
        
        p = Produto(
            nome=fake.bothify(text='Lanche ??-##'),
            preco_compra=p_compra,
            preco_venda=p_venda,
            data_compra="2026-03-26",
            data_validade="2026-12-31",
            quantidade=random.randint(10, 100)
        )
        produtos_fakes.append(p)
    return produtos_fakes
