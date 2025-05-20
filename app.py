import streamlit as st
from scripts.ipca import baixar_ipca
import altair as alt

st.set_page_config(page_title="Indicadores Econômicos do Brasil", layout="centered")

st.title("📊 Dashboard Econômico do Brasil")
st.markdown("Visualize indicadores atualizados de forma simples e didática.")

# Carregar dados
ipca_df = baixar_ipca()
ipca_df = ipca_df.sort_values("data")

# Gráfico
st.subheader("Inflação (IPCA - mensal)")
chart = alt.Chart(ipca_df.tail(36)).mark_line().encode(
    x='data:T',
    y='valor:Q',
    tooltip=['data:T', 'valor']
).properties(width=600)

st.altair_chart(chart, use_container_width=True)
st.caption("Fonte: Banco Central do Brasil (SGS - série 433)")
