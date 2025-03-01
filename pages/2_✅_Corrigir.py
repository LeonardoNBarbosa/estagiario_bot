import streamlit as st
import time
import AI

chave = st.secrets["GEMINI_CHAVE"]

st.subheader("Correção de Código ✅")

ai_saudacao = st.chat_message("ai")
ai_saudacao.write("Olá, informe no chat o código para que eu ajude a encontrar o erro ou problema.")

st.session_state.codigo = st.chat_input("Cole seu código aqui...")

if st.session_state.codigo is None:
    pass
else:
    usuario = st.chat_message("user")
    usuario.write(st.session_state.codigo)
        
    with st.chat_message("ai"):
        with st.spinner("Analisando código..."):
            time.sleep(4)
            st.session_state.correcao = AI.correcao_codigo(chave, st.session_state.codigo)

            if 'correcao' in st.session_state:
                st.snow()
                st.write(st.session_state.correcao)