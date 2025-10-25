import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh 
# IMPORTAR A FUNÇÃO, NÃO A VARIÁVEL
from dataset import get_data_from_json 

# ----------------------------------------------------
# 1. Configurar o Autorefresh para forçar o script a re-executar a cada 5s
st_autorefresh(interval=5000, key="data_refresh_key") 
# ----------------------------------------------------

st.set_page_config(layout='wide')
st.title("Dashboard de Vendas ")

# 2. Chamar a função para obter o DataFrame ATUALIZADO
# O cache no dataset.py fará com que a leitura do JSON só ocorra quando necessário.
df = get_data_from_json()

# 3. Lógica do Streamlit
if not df.empty:
    st.sidebar.title("Filtro de Vendedores")

    # Garanta que a coluna existe
    if 'Vendedor' in df.columns:
        filtro_vendedor = st.sidebar.multiselect(
            'Vendedores',
            df['Vendedor'].unique(),
        )

        if filtro_vendedor:
            df_filtrado = df[df['Vendedor'].isin(filtro_vendedor)]
        else:
            df_filtrado = df # Usa o DF completo se não houver filtro

        # Exemplo de Métrica (Ajustar para as suas colunas de preço)
        if 'Preço' in df_filtrado.columns:
             receita_total = df_filtrado['Preço'].sum()
             st.metric(label="Receita Total Filtrada", value=f"R$ {receita_total:,.2f}") 
        
        tab1, tab2, tab3 = st.tabs(['Dataset', 'Receita', 'Vendedores'])
        
        with tab1:
            st.dataframe(df_filtrado)
    else:
        st.error("Coluna 'Vendedor' não encontrada no DataFrame.")

else:
    st.warning("Não foi possível carregar os dados. Verifique o arquivo JSON em 'dados/vendas.json'.")

