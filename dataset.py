import json
import os
import time
import pandas as pd
import streamlit as st # Necessário para usar o decorador @st.cache_data

# O DECORADOR DE CACHE É ESSENCIAL PARA A ATUALIZAÇÃO
# ttl=5: O cache expira a cada 5 segundos. Quando o cache expira,
# a função é executada novamente, lendo o JSON fresco.
@st.cache_data(ttl=60)
def get_data_from_json():
    """
    Carrega, processa e retorna o DataFrame de vendas.
    """
    # A variável 'file' e o bloco 'with open(...)' garantem 
    # que o arquivo seja lido e fechado corretamente, mesmo em caso de erro.
    try:
        # Usamos 'with open' para garantir que o arquivo seja fechado automaticamente
        with open('dados/vendas.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        # Criação do DataFrame
        df = pd.DataFrame.from_dict(data)
        
        # Tratamento de Data (Sua lógica original)
        # O formato %d/%m/%Y está correto
        df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

        # O print é útil para debug na nuvem, mas pode ser removido depois.
        print(f"Dados recarregados e processados em: {time.strftime('%H:%M:%S')}") 
        
        # Remova o 'df.to_csv' e outros prints desnecessários que não são o foco do Streamlit
        
        return df

    except FileNotFoundError:
        print("ERRO: Arquivo 'dados/vendas.json' não encontrado.")
        return pd.DataFrame()
    except Exception as e:
        print(f"ERRO ao carregar ou processar dados: {e}")
        return pd.DataFrame()