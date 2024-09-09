from cgitb import text
from multiprocessing import Value
from os import write
from turtle import onclick, onscreenclick
from typing import List
import streamlit as st
import Pages.Cliente.Create as PageCreateCliente
import Pages.Cliente.List as PageListCliente
import services.database as db
import Controllers.UsuarioController as UsuarioController

db.conectar_banco()

# Função para exibir a página de login
def login_page():
    st.title("Login")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Login"):
        success, message = UsuarioController.login_usuario(username, password)
        if success:
            st.session_state['logged_in'] = True
            st.session_state['username'] = username
            st.success(message)
            st.query_params.clear()  # Forçar recarga da página
        else:
            st.error(message)

# Função para exibir a página de cadastro
def cadastro_page():
    st.title("Cadastro")
    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")
    if st.button("Cadastrar"):
        success, message = UsuarioController.cadastrar_usuario(username, password)
        if success:
            st.success(message)
        else:
            st.error(message)

# Função para exibir a página principal
def main_page():
    st.sidebar.title(f"Bem-vindo, {st.session_state['username']}")
    if st.sidebar.button("Logout"):
        st.session_state['logged_in'] = False
        st.query_params.clear()  # Forçar recarga da página

    Page_cliente = st.sidebar.selectbox(
        'Cliente', ['Incluir', 'Consultar'], 0)

    if Page_cliente == 'Consultar':
        PageListCliente.List()

    if Page_cliente == 'Incluir':
        st.query_params.clear()
        PageCreateCliente.Create()

# Verificar se o usuário está logado
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if st.session_state['logged_in']:
    main_page()
else:
    page = st.sidebar.selectbox('Página', ['Login', 'Cadastro'])
    if page == 'Login':
        login_page()
    else:
        cadastro_page()