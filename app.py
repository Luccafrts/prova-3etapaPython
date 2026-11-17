import plotly.express as px
import pandas as pd
import streamlit as st


df = pd.read_csv("dados_transporte_bh.csv", sep=";")
df.columns = df.columns.str.strip()
df["LINHA"] = df["LINHA"].astype(str).str.strip()

df = df[~df["PC"].isin([0, 3])]


viagens = df.groupby("LINHA").size().reset_index(name="viagens")
top_10 = viagens.sort_values(by="viagens", ascending=False).head(10)

st.title("Transporte Coletivo de Belo Horizonte")

st.title("Transporte Coletivo de Belo Horizonte")

opcao = st.sidebar.radio(
    "Escolha a visualização:",
    ["Tabela", "Gráfico"]
)

if opcao == "Tabela":
    st.header("As 10 linhas com mais viagens (Tabela)")
    st.dataframe(top_10, use_container_width=True, hide_index=True)
    
elif opcao =="Gráfico":
    st.header("As 10 linhas com mais viagens (grafico)")
    fig.px