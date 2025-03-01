import streamlit as st

st.set_page_config(
    layout="wide",
    page_title="Estagiário BOT",
    page_icon="🤖"
)

col1, col2 = st.columns([4, 11])

with col1:
    st.image("arquivos/robo_2.0.png", width=300)

with col2:
    st.title("🤖 Estagiário BOT")

    st.markdown("\n")

    st.markdown("#### Saudações")
    st.markdown("""
                Seja bem vindo!
                Sou o ***Estagiário BOT*** e estou aqui para facilitar sua programação do dia a dia.
                """)
    st.markdown("Está com um código bugado? Quer converter de uma linguagem pra outra?")
    st.markdown("Resolva seus problemas com minha ajuda, economize tempo e foque no que importa.")

    st.page_link("pages/2_✅_Corrigir.py", label="Corrigir", icon="1️⃣")
    st.page_link("pages/3_🔮_Converter.py", label="Converter", icon="2️⃣")
    st.page_link("http://www.google.com", label="Repositório Github", icon="🔗")