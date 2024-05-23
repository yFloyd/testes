# Projeto de Análise de Carrinhos de Compras

Este projeto tem como objetivo buscar, processar e exibir dados de carrinhos de compras e categorias de produtos a partir de uma API.

## Estrutura do Projeto

O projeto está dividido em dois arquivos principais:

1. `functions.py`: Contém funções auxiliares para buscar e processar dados.
2. `main.ipynb`: Contém a função `main` que orquestra a execução do código.

## Funcionalidades

### Arquivo `functions.py`

Este arquivo contém as seguintes funções:

- `fetch_data(url)`: Realiza uma conexão via API para buscar dados a partir de uma URL.
- `process_cart_data(cart_data)`: Processa os dados do carrinho para extrair e normalizar informações sobre produtos e datas.
- `process_category_data(category_data)`: Processa os dados de categoria para extrair IDs de produtos e suas categorias.
- `merge_cart_with_category(df_cart, df_category)`: Faz o merge dos dados do carrinho com os dados de categoria com base nos IDs dos produtos.
- `aggregate_cart_data(df_cart_category)`: Agrega os dados do carrinho para encontrar a data mais recente e somar as quantidades por usuário e categoria.

### Arquivo `main.ipynb`

Este notebook contém a função `main` que executa o fluxo completo do projeto:

- Busca os dados dos carrinhos e das categorias usando as funções de `functions.py`.
- Processa e agrega os dados.
- Transforma em CSV o resultado final.
