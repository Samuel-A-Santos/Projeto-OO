import streamlit as st
import Controllers.FuncionarioController as FuncionarioController
import models.Funcionario as funcionario
import models.Endereco as endereco

def Create():
    idAlteracao = st.experimental_get_query_params()
    funcionarioRecuperado = None
    if idAlteracao.get("id") is not None:
        idAlteracao = idAlteracao.get("id")[0]
        funcionarioRecuperado = FuncionarioController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(id=str(funcionarioRecuperado.id))
        st.title("Alterar funcionário")
    else:
        st.title("Incluir funcionário")

    with st.form(key="include_funcionario"):
        listOccupation = ["Desenvolvedor", "Músico", "Designer", "Professor"]
        if funcionarioRecuperado is None:
            input_name = st.text_input(label="Insira o seu nome")
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1)
            input_occupation = st.selectbox(label="Selecione sua profissão", options=listOccupation)
            input_rua = st.text_input(label="Insira a rua")
            input_cidade = st.text_input(label="Insira a cidade")
            input_estado = st.text_input(label="Insira o estado")
            input_cep = st.text_input(label="Insira o CEP")
        else:
            input_name = st.text_input(label="Insira o seu nome", value=funcionarioRecuperado.nome)
            input_age = st.number_input(label="Insira sua idade", format="%d", step=1, value=funcionarioRecuperado.idade)
            input_occupation = st.selectbox(label="Selecione sua profissão", options=listOccupation, index=listOccupation.index(funcionarioRecuperado.profissao))
            input_rua = st.text_input(label="Insira a rua", value=funcionarioRecuperado.endereco.rua)
            input_cidade = st.text_input(label="Insira a cidade", value=funcionarioRecuperado.endereco.cidade)
            input_estado = st.text_input(label="Insira o estado", value=funcionarioRecuperado.endereco.estado)
            input_cep = st.text_input(label="Insira o CEP", value=funcionarioRecuperado.endereco.cep)
        input_button_submit = st.form_submit_button("Enviar")

    if input_button_submit:
        novo_endereco = endereco.Endereco(rua=input_rua, cidade=input_cidade, estado=input_estado, cep=input_cep)
        if funcionarioRecuperado is None:
            novo_funcionario = funcionario.Funcionario(nome=input_name, idade=input_age, profissao=input_occupation, endereco=novo_endereco)
            FuncionarioController.Incluir(novo_funcionario, novo_endereco)
            st.success("Funcionário incluído com sucesso!")
        else:
            st.experimental_set_query_params(id=str(funcionarioRecuperado.id))
            funcionarioRecuperado.nome = input_name
            funcionarioRecuperado.idade = input_age
            funcionarioRecuperado.profissao = input_occupation
            FuncionarioController.Alterar(funcionarioRecuperado, novo_endereco)
            st.success("Funcionário alterado com sucesso!")