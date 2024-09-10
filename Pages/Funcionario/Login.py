import streamlit as st
import Controllers.FuncionarioController as FuncionarioController
import models.Funcionario as funcionario

def Login():
    st.title("Login de Funcionário")
    username = st.text_input("Nome de Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Login"):
        funcionario = FuncionarioController.SelecionarByUsername(username)
        if funcionario and funcionario.password == password:
            st.session_state['logged_in_funcionario'] = True
            st.session_state['funcionario_id'] = str(funcionario.id)
            st.success("Login bem-sucedido!")
            st.experimental_set_query_params()
        else:
            st.error("Credenciais inválidas")