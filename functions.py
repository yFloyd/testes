import requests
import pandas as pd

import requests

def fetch_data(url):
    """Realizar conexão via API"""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao tentar acessar {url}: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Erro de conexão ao tentar acessar {url}: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Tempo de conexão esgotado ao tentar acessar {url}: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro ao tentar acessar {url}: {req_err}")
    return None


def process_cart_data(cart_data):
    """Transformar em dataframe, limpando e selecionando as colunas"""
    df_cart = pd.json_normalize(cart_data, 'products', ['userId', 'date'])[['userId', 'date', 'productId', 'quantity']]
    df_cart['date'] = pd.to_datetime(df_cart['date']).dt.strftime('%Y-%m-%d %H:%M:%S')
    return df_cart

def process_category_data(category_data):
    """Transformar em dataframe"""
    return pd.json_normalize(category_data)[['id', 'category']]

def merge_cart_with_category(df_cart, df_category):
    """Realizar merge entre as duas tabelas"""
    df_cart_category = df_cart.merge(df_category, left_on='productId', right_on='id', how='left')
    df_cart_category.drop(['productId', 'id'], axis=1, inplace=True)
    return df_cart_category

def aggregate_cart_data(df_cart_category):
    """Realizo uma limpeza tirando colunas desnecessárias, somo as categorias por usuario, e pego a categoria que tem produtos no carrinho"""
    df_cart_category['date'] = pd.to_datetime(df_cart_category['date'])
    df_cart_category['date'] = df_cart_category.groupby('userId')['date'].transform('max')
    df_cart_category = df_cart_category.groupby(['userId', 'category']).agg({'quantity': 'sum', 'date': 'max'}).reset_index()
    df_cart_category.sort_values(by=['userId', 'quantity'], ascending=[True, False], inplace=True)
    df_cart_category = df_cart_category.groupby('userId').first().reset_index()
    return df_cart_category.rename(columns={
        'userId': 'id_usuario',
        'category': 'categoria_moda_do_carrinho_por_usuario',
        'quantity': 'quantidade',
        'date': 'data_mais_recente'
    })
