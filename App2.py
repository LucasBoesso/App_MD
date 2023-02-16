import streamlit as st
import numpy as np

st.write("# Novo aplicativo")

btn1 = st.button("Novo botão")

if btn1 == True:
    st.write("### Sua aplicação está funcionando")


l= np.random.randint(5,20,10)
st.write(l)