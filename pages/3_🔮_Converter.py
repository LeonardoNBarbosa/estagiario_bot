import streamlit as st
import time
import AI

chave = st.secrets["GEMINI_CHAVE"]

st.subheader("Conversão entre Linguagens 🔮")

with st.chat_message("ai"):
    st.write("Olá, escolha abaixo a linguagem original do seu código e depois a que deseja converter.")

    col1, col2 = st.columns(2)
        
    with col1:
        linguagem_atual = st.selectbox(
            "Linguagem Atual",
            ("Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript"),
            index=None,
            placeholder=("Selecionar")
        )

    with col2:
        linguagem_conversao = st.selectbox(
            "Linguagem para Conversão",
            ("Python", "Java", "C", "C++", "C#", "JavaScript", "TypeScript"),
            index=None,
            placeholder=("Selecionar")
        )

    if linguagem_atual and linguagem_conversao is not None:
        st.session_state.codigo = st.text_area(
            " ",
            placeholder="Cole seu código aqui..."
        )

        if st.button("Converter"):
            with st.spinner("Convertendo..."):
                time.sleep(4)
                st.session_state.conversao = AI.conversao_codigo(chave, linguagem_atual, linguagem_conversao, st.session_state.codigo)

                if 'conversao' in st.session_state:
                    st.balloons()
                    st.markdown(f":green[**{linguagem_conversao}**]")
                    st.write(st.session_state.conversao)
