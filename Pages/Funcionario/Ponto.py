import streamlit as st
import Controllers.FuncionarioController as FuncionarioController

def Ponto():
    if 'funcionario_id' not in st.session_state:
        st.error("Você precisa estar logado para acessar esta página.")
        return

    funcionario_id = st.session_state['funcionario_id']
    pontos = FuncionarioController.SelecionarPontos(funcionario_id)

    st.title("Registro de Ponto")
    if st.button("Registrar Entrada"):
        ponto = FuncionarioController.RegistrarPontoEntrada(funcionario_id)
        if ponto:
            st.success(f"Entrada registrada em {ponto.entrada_formatada}")
        else:
            st.error("Erro: Já existe um ponto registrado hoje.")

    if st.button("Registrar Saída"):
        ponto = FuncionarioController.RegistrarPontoSaida(funcionario_id)
        if ponto:
            st.success(f"Saída registrada em {ponto.saida_formatada}")
        else:
            st.error("Erro ao registrar saída")

    st.header("Histórico de Pontos")
    for ponto in pontos:
        st.write(f"Data: {ponto.data_formatada}, Entrada: {ponto.entrada_formatada}, Saída: {ponto.saida_formatada}")