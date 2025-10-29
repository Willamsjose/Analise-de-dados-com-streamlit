import streamlit as st
import plotly.express as px
from dataset import df, get_data # Import df and the data loading function
from utils import format_number

# Function to clear the cache for the data loading function
def clear_data_cache():
    # st.cache_data applies to get_data, so we clear the cache for it
    get_data.clear() 

st.set_page_config(layout='wide')
st.title("Dashboard de Vendas")

# Add the button to clear the cache and hence force a reload on rerun
st.button(
    'Atualizar Dados', 
    on_click=clear_data_cache, 
    help='Clique para limpar o cache e recarregar os dados imediatamente.'
)

# After clearing the cache, Streamlit will rerun the script, 
# and df = get_data() in dataset.py will be executed again, reloading the data.

aba1, aba2, aba3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
with aba1:
    st.dataframe(df)
with aba2:
    coluna1, coluna2 = st.columns(2)
    with coluna1:
        st.metric('Receita Total', format_number(df['Preço'].sum(), 'R$'))
    with coluna2:
        st.metric('Quantidade de Vendas', format_number(df.shape[0]))