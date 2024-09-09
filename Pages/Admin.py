import streamlit as st
import Controllers.ClienteController as ClienteController
import Controllers.UsuarioController as UsuarioController

def Admin():
    st.title("Administração do Banco de Dados")

    st.header("Clientes")
    clientes = ClienteController.SelecionarTodos()
    for cliente in clientes:
        st.write(f"ID: {cliente.id}, Nome: {cliente.nome}, Idade: {cliente.idade}, Profissão: {cliente.profissao}")

    st.header("Usuários")
    usuarios = UsuarioController.SelecionarTodos()
    for usuario in usuarios:
        st.write(f"ID: {usuario.id}, Username: {usuario.username}")