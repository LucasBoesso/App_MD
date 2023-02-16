import streamlit as st

st.write("# Novo aplicativo")

btn1 = st.button("Novo botão")

if btn1 == True:
    st.write("### Sua aplicação está funcionando")