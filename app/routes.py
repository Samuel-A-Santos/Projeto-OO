from flask import render_template, request, redirect, url_for, session, flash
import Controllers.UsuarioController as UsuarioController
import Controllers.ClienteController as ClienteController
from app.models import Cliente  # Adicione esta linha

def init_routes(app):
    @app.route('/')
    def index():
        if 'logged_in' in session and session['logged_in']:
            return redirect(url_for('main_page'))
        return redirect(url_for('login_page'))

    @app.route('/login', methods=['GET', 'POST'])
    def login_page():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            success, message = UsuarioController.login_usuario(username, password)
            if success:
                session['logged_in'] = True
                session['username'] = username
                flash(message, 'success')
                return redirect(url_for('main_page'))
            else:
                flash(message, 'danger')
        return render_template('login.html')

    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro_page():
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            success, message = UsuarioController.cadastrar_usuario(username, password)
            if success:
                flash(message, 'success')
            else:
                flash(message, 'danger')
        return render_template('cadastro.html')

    @app.route('/main')
    def main_page():
        if 'logged_in' not in session or not session['logged_in']:
            return redirect(url_for('login_page'))
        return render_template('main.html', username=session['username'])

    @app.route('/logout')
    def logout():
        session.pop('logged_in', None)
        session.pop('username', None)
        return redirect(url_for('login_page'))

    @app.route('/cliente/incluir', methods=['GET', 'POST'])
    def incluir_cliente():
        if request.method == 'POST':
            nome = request.form['nome']
            idade = request.form['idade']
            profissao = request.form['profissao']
            ClienteController.Incluir(Cliente(nome=nome, idade=idade, profissao=profissao))
            flash('Cliente incluído com sucesso!', 'success')
            return redirect(url_for('listar_clientes'))
        return render_template('cliente/create.html')

    @app.route('/cliente/consultar')
    def listar_clientes():
        clientes = ClienteController.SelecionarTodos()
        return render_template('cliente/list.html', clientes=clientes)

    @app.route('/cliente/excluir/<id>')
    def excluir_cliente(id):
        ClienteController.Excluir(id)
        flash('Cliente excluído com sucesso!', 'success')
        return redirect(url_for('listar_clientes'))

    @app.route('/cliente/alterar/<id>', methods=['GET', 'POST'])
    def alterar_cliente(id):
        cliente = ClienteController.SelecionarById(id)
        if request.method == 'POST':
            cliente.nome = request.form['nome']
            cliente.idade = request.form['idade']
            cliente.profissao = request.form['profissao']
            ClienteController.Alterar(cliente)
            flash('Cliente alterado com sucesso!', 'success')
            return redirect(url_for('listar_clientes'))
        return render_template('cliente/create.html', cliente=cliente)