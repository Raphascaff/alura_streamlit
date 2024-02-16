# ----- Import librarires ------ #
from utils import formata_numero
import streamlit as st
import requests
import pandas as pd
import plotly.express as px 

### ---- End ------##

# ----- Start Dashboard ------ #


st.title('DASHBOARD DE VENDAS :shopping_trolley:')

# ---- Get data ----- #

url = 'https://labdados.com/produtos'
response = requests.get(url)
dados = pd.DataFrame.from_dict(response.json())

# --- Show data ---- #


coluna1, coluna2 = st.columns(2)
with coluna1:
    st.metric('Receita', formata_numero(dados['Preço'].sum(), 'R$'))
with coluna2:
    st.metric('Quantidade de vendas', formata_numero(dados.shape[0]))

st.dataframe(dados)
