import pandas as pd
import json
import streamlit as st
from io import BytesIO # Necessário para manipular o conteúdo lido

# 1. Defina o URI do S3 aqui (Substitua <SEU_BUCKET> e <SUA_CHAVE>)
S3_URI = "s3://arn:aws:s3:::dado-vendas-json/Dados/vendas.json" 

@st.cache_data(ttl=5)
def get_data_from_json():
    """
    Carrega, processa e retorna o DataFrame de vendas do S3.
    """
    try:
        # 1. Leitura Direta do S3 usando Pandas e s3fs
        # O s3fs gerencia a autenticação via IAM Role (ver Fase 2)
        df = pd.read_json(S3_URI)
        
        # 2. Tratamento de Data (Sua lógica original)
        df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')
        
        return df

    except Exception as e:
        # Se houver erro, exiba no Streamlit
        st.error(f"ERRO ao carregar dados do S3: {e}")
        return pd.DataFrame()