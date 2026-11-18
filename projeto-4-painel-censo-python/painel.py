import pandas as pd
import streamlit as st

def classifica_porte(total):
    if total <= 200:
        return "Pequena"
    elif total <= 400:
        return "Média"
    return "Grande"

@st.cache_data
def carregar_dados():
    dados = pd.read_csv("escolas_sp_regioes_2024_geo.csv")
    dados["matriculas"] = pd.to_numeric(dados["matriculas"], errors="coerce").fillna(0)
    dados["porte"] = dados["matriculas"].apply(classifica_porte)
    return dados

censo = carregar_dados()
st.title("Painel de escolas de regiões de SP")
st.caption("Censo Escolar 2024 — escolas em atividade de quatro regiões paulistas")
regioes = ["Todas"] + sorted(censo["regiao"].dropna().unique().tolist())
regiao = st.selectbox("Escolha a região", regioes)
if regiao != "Todas":
    censo = censo.loc[censo["regiao"] == regiao].copy()
municipios = ["Todos"] + sorted(censo["municipio"].dropna().unique().tolist())
municipio = st.selectbox("Escolha o município", municipios)
if municipio != "Todos":
    censo = censo.loc[censo["municipio"] == municipio].copy()
col1, col2 = st.columns(2)
col1.metric("Quantidade de escolas", f"{len(censo):,}".replace(",", "."))
col2.metric("Total de matrículas", f"{int(censo['matriculas'].sum()):,}".replace(",", "."))
st.subheader("Escolas por porte")
st.bar_chart(censo["porte"].value_counts().reindex(["Pequena", "Média", "Grande"], fill_value=0))
st.subheader("Escolas por dependência administrativa")
st.bar_chart(censo["dependencia"].fillna("Não informado").value_counts())
st.subheader("Escolas por abastecimento de água")
st.bar_chart(censo["agua"].fillna("Não informado").value_counts())
st.subheader("Escolas por fonte de energia")
st.bar_chart(censo["energia"].fillna("Não informado").value_counts())
st.subheader("Mapa das escolas")
coordenadas = censo[["latitude", "longitude"]].apply(pd.to_numeric, errors="coerce").dropna()
if coordenadas.empty:
    st.info("Não há escolas com coordenadas disponíveis para esta seleção.")
else:
    st.map(coordenadas)
st.subheader("Lista das escolas")
st.dataframe(censo[["regiao", "municipio", "escola", "dependencia", "matriculas", "porte"]], use_container_width=True, hide_index=True)
