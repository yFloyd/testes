from functions import fetch_data, process_cart_data, process_category_data, merge_cart_with_category, aggregate_cart_data

def main():
    """Função principal, para para transformar em CSV"""
    cart_url = 'https://fakestoreapi.com/carts'
    category_url = 'https://fakestoreapi.com/products'

    # Função de conexao API
    cart_data = fetch_data(cart_url)
    category_data = fetch_data(category_url)

    # Função que transforma em Dataframe
    df_cart = process_cart_data(cart_data)
    df_category = process_category_data(category_data)

    # Função de transformação dos dados
    df_cart_category = merge_cart_with_category(df_cart, df_category)
    df_cart_category = aggregate_cart_data(df_cart_category)

    # Transformar em CSV
    df_cart_category.to_csv('df_cart_category.csv')

main()
