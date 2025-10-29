import json
import pandas as pd
import streamlit as st  

@st.cache_data(ttl=5, show_spinner='Carregando dados...')
def get_data():
    file = open('vendas.json', encoding='utf-8')
    data = json.load(file)
    file.close()

    df = pd.DataFrame.from_dict(data)

    # Convert 'Data da Compra' column if present and needed
    # if 'Data da Compra' in df.columns:
    #     df['Data da Compra'] = pd.to_datetime(df['Data da Compra'], format='%d/%m/%Y')

    print(df) # for debugging purposes if needed
    return df

df = get_data()