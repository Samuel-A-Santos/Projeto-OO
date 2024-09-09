import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente

def Create():
    idAlteracao = st.experimental_get_query_params()
    clienteRecuperado = None
    if idAlteracao.get("id") is not None:
        idAlteracao = idAlteracao.get("id")[0]
        clienteRecuperado = ClienteController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(id=str(clienteRecuperado.id))
        st.title("Alterar cliente")
    else:
        st.title("Incluir cliente")

    with st.form(key="include_cliente"):
        listOccupation = ["Desenvolvedor", "Músico", "Designer", "Professor"]
        if clienteRecuperado is None:
            input_name = st.text_input(label="Insira o seu nome")
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
            input_occupation = st.selectbox(label="Selecione sua profissão", options=listOccupation)
        else:
            input_name = st.text_input(label="Insira o seu nome", value=clienteRecuperado.nome)
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1, value=clienteRecuperado.idade)
            input_occupation = st.selectbox(label="Selecione sua profissão", options=listOccupation, index=listOccupation.index(clienteRecuperado.profissao))
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        if clienteRecuperado is None:
            novo_cliente = cliente.Cliente(nome=input_name, idade=input_age, profissao=input_occupation)
            ClienteController.Incluir(novo_cliente)
            st.success("Cliente incluído com sucesso!")
        else:
            st.experimental_set_query_params(id=str(clienteRecuperado.id))
            clienteRecuperado.nome = input_name
            clienteRecuperado.idade = input_age
            clienteRecuperado.profissao = input_occupation
            ClienteController.Alterar(clienteRecuperado)
            st.success("Cliente alterado com sucesso!")