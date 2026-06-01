import streamlit as st
import pandas as pd
import plotly.express as px


# CONFIGURATION GLOBALE

st.set_page_config(
    page_title="Food Waste Analytics",
    page_icon="🌍",
    layout="wide"
)


# CSS CUSTOM — DESIGN PREMIUM

st.markdown("""
<style>

body {
    background-color: #0e1117;
}

[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #0e1117 0%, #1a1f2b 100%);
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif;
    font-weight: 600;
}

.sidebar .sidebar-content {
    background: #111827;
}

[data-testid="stSidebar"] {
    background: #111827;
}

.metric-card {
    padding: 20px;
    border-radius: 15px;
    background: rgba(255,255,255,0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    text-align: center;
}

.metric-title {
    font-size: 18px;
    color: #cbd5e1;
}

.metric-value {
    font-size: 28px;
    font-weight: bold;
    color: #ffffff;
}

</style>
""", unsafe_allow_html=True)


# TITRE

st.markdown(
    "<h1 style='text-align:center; color:white;'>🌍 Food Waste Analytics Dashboard</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center; color:#94a3b8; font-size:18px;'>Analyse interactive du gaspillage alimentaire mondial (UNEP)</p>",
    unsafe_allow_html=True
)


# CHARGEMENT DES DONNÉES

df = pd.read_csv("data/clean/FoodWasteAI_clean.csv")


# SIDEBAR

st.sidebar.markdown("## 🔍 Filtres")
regions = ["Toutes les régions"] + sorted(df["region"].unique().tolist())
selected_region = st.sidebar.selectbox("🌎 Choisir une région", regions)

if selected_region != "Toutes les régions":
    df_filtered = df[df["region"] == selected_region]
else:
    df_filtered = df


# INDICATEURS CLÉS

st.markdown("### 📌 Indicateurs clés")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("<div class='metric-title'>Gaspillage total moyen</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-value'>{df_filtered['combined_figures_kg_capita_year'].mean():.1f} kg/hab/an</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("<div class='metric-title'>Gaspillage ménages moyen</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-value'>{df_filtered['household_estimate_kg_capita_year'].mean():.1f} kg/hab/an</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div class='metric-card'>", unsafe_allow_html=True)
    st.markdown("<div class='metric-title'>Nombre de pays</div>", unsafe_allow_html=True)
    st.markdown(f"<div class='metric-value'>{df_filtered['country'].nunique()}</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# TOP 10 PAYS

st.markdown("### 🏆 Top 10 des pays les plus concernés")

top10 = df_filtered.sort_values(
    by="combined_figures_kg_capita_year",
    ascending=False
).head(10)

fig_top10 = px.bar(
    top10,
    x="country",
    y="combined_figures_kg_capita_year",
    title="Top 10 des pays selon le gaspillage alimentaire total",
    color="combined_figures_kg_capita_year",
    color_continuous_scale="Reds"
)

st.plotly_chart(fig_top10, use_container_width=True)


# GASPILLAGE PAR RÉGION

st.markdown("### 🌍 Gaspillage moyen par région")

region_mean = (
    df.groupby("region")["combined_figures_kg_capita_year"]
    .mean()
    .reset_index()
    .sort_values(by="combined_figures_kg_capita_year", ascending=False)
)

fig_region = px.bar(
    region_mean,
    x="region",
    y="combined_figures_kg_capita_year",
    title="Gaspillage alimentaire moyen par région",
    color="combined_figures_kg_capita_year",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_region, use_container_width=True)


# TABLEAU DES DONNÉES

st.markdown("### 🔎 Données filtrées")
st.dataframe(df_filtered, use_container_width=True)
