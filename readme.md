Cantina Fatec

Projeto acadêmico desenvolvido para as disciplinas Estrutura de Dados e Linguagem de Programação 2 da Fatec Rio Claro.

Estrutura do Projeto
- main.py: Interface de terminal e menu principal.
- models.py: Classes base (Produto, Pagamento, Consumo).
- estrutura.py: Lógica de Fila e Listas de dados.
- services.py: Regras de negócio (Baixa de estoque e Vendas).
- utils.py: Persistência com Pickle e geração de dados sintéticos (Faker).

Funcionalidades
- Estoque Inteligente: Baixa automática por lotes (mais antigos primeiro).
- Vendas Reais: Registro financeiro com data/hora e cálculo de lucro.
- Massa de Dados: Geração de lanches reais (Coxinha, Pão de Queijo) para testes.
- Persistência: Salvamento automático em arquivos .pkl na pasta /data.
  
