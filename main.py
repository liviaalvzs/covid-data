import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv')

df = df.rename(columns={'newDeaths':'Novos óbitos', 'newCases': 'Novos Casos', 'deaths_per_100k_inhabitants':'Óbitos por 100 mil habitantes','totalCases_per_100k_inhabitants': 'Casos por 100 mil habitantes'})

estados = list(df['state'].unique())
estado_selecionado = st.sidebar.selectbox('Selecionar estado', estados)

colunas = ['Novos óbitos', 'Novos Casos', 'Óbitos por 100 mil habitantes', 'Casos por 100 mil habitantes']
info_selecionada = st.sidebar.selectbox('Selecionar tipo de informação', colunas)

df = df[df['state'] == estado_selecionado]

fig = px.line(df, x='date', y=info_selecionada, title= info_selecionada + '-' + estado_selecionado)
fig.update_layout( xaxis_title='Data', yaxis_title=info_selecionada.upper(), title = {'x':0.5})

st.title('Dados COVID-19 - Brasil 💊')
st.write('Use o menu lateral para selecionar a informação que deseja e também o estado a ser analisado.')
st.plotly_chart(fig, use_container_width=True)

st.write('Dados obtidos a partir de https://github.com/wcota/covid19br')
st.write('Projeto desenvolvido por @liviaalvzs | https://github.com/liviaalvzs/dados-covid 🤎')



