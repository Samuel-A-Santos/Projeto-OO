import streamlit as st
import Controllers.ClienteController as ClienteController
import models.Cliente as cliente
import models.Endereco as endereco

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
            input_rua = st.text_input(label="Insira a rua")
            input_cidade = st.text_input(label="Insira a cidade")
            input_estado = st.text_input(label="Insira o estado")
            input_cep = st.text_input(label="Insira o CEP")
        else:
            input_name = st.text_input(label="Insira o seu nome", value=clienteRecuperado.nome)
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1, value=clienteRecuperado.idade)
            input_occupation = st.selectbox(label="Selecione sua profissão", options=listOccupation, index=listOccupation.index(clienteRecuperado.profissao))
            input_rua = st.text_input(label="Insira a rua", value=clienteRecuperado.endereco.rua)
            input_cidade = st.text_input(label="Insira a cidade", value=clienteRecuperado.endereco.cidade)
            input_estado = st.text_input(label="Insira o estado", value=clienteRecuperado.endereco.estado)
            input_cep = st.text_input(label="Insira o CEP", value=clienteRecuperado.endereco.cep)
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        novo_endereco = endereco.Endereco(rua=input_rua, cidade=input_cidade, estado=input_estado, cep=input_cep)
        if clienteRecuperado is None:
            novo_cliente = cliente.Cliente(nome=input_name, idade=input_age, profissao=input_occupation, endereco=novo_endereco)
            ClienteController.Incluir(novo_cliente, novo_endereco)
            st.success("Cliente incluído com sucesso!")
        else:
            st.experimental_set_query_params(id=str(clienteRecuperado.id))
            clienteRecuperado.nome = input_name
            clienteRecuperado.idade = input_age
            clienteRecuperado.profissao = input_occupation
            ClienteController.Alterar(clienteRecuperado, novo_endereco)
            st.success("Cliente alterado com sucesso!")