import streamlit as st
import plotly.express as px
from dataset import df  

st.set_page_config(layout="wide")
st.title("Dashboard de Vendas :shopping_cart:")


aba1, aba2, aba3 = st.tabs(["dataset", "Receita", "Vendedores"])

with aba1:
    st.dataframe(df)    

with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        receita_total = df['PreÃ§o'].sum()

# Dividir por 1 milhão
receita_em_milhoes = receita_total / 1000000

# Formatar como string com 2 casas decimais e o 'M'
valor_formatado = f"R$ {receita_em_milhoes:,.2f}M" 

st.metric('Receita Total', valor_formatado)
with coluna2:
    st.metric('Quantidade de Vendas', df.shape[0])