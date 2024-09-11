from flask import render_template, request, redirect, url_for, session, flash
import Controllers.UsuarioController as UsuarioController
import Controllers.FuncionarioController as FuncionarioController
from models.Funcionario import Funcionario
from models.Endereco import Endereco
from bson import ObjectId
import services.database as db

# Certifique-se de que a conexão com o banco de dados é inicializada
print("Inicializando a conexão com o banco de dados nas rotas...")
db.conectar_banco()

def init_routes(app):
    @app.route('/')
    def index():
        print("Rota / acessada")
        if 'logged_in' in session and session['logged_in']:
            return redirect(url_for('main_page'))
        return redirect(url_for('login_page'))

    @app.route('/login', methods=['GET', 'POST'])
    def login_page():
        print("Rota /login acessada")
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            print(f"Tentativa de login com usuário: {username}")
            success, message = UsuarioController.login_usuario(username, password)
            if success:
                session['logged_in'] = True
                session['username'] = username
                session['is_admin'] = UsuarioController.is_admin(username)
                funcionario = FuncionarioController.SelecionarByUsername(username)
                if funcionario:
                    session['funcionario_id'] = str(funcionario.id)
                    session['logged_in_funcionario'] = True
                flash(message, 'success')
                return redirect(url_for('main_page'))
            else:
                flash(message, 'danger')
        return render_template('login.html')

    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro_page():
        print("Rota /cadastro acessada")
        if request.method == 'POST':
            nome = request.form['nome']
            idade = request.form['idade']
            profissao = request.form['profissao']
            rua = request.form['rua']
            cidade = request.form['cidade']
            estado = request.form['estado']
            cep = request.form['cep']
            username = request.form['username']
            password = request.form['password']
            print(f"Tentativa de cadastro com usuário: {username}")
            success, message = UsuarioController.cadastrar_usuario(nome, idade, profissao, rua, cidade, estado, cep, username, password)
            if success:
                session['logged_in'] = True
                session['username'] = username
                session['is_admin'] = UsuarioController.is_admin(username)
                funcionario = FuncionarioController.SelecionarByUsername(username)
                if funcionario:
                    session['funcionario_id'] = str(funcionario.id)
                    session['logged_in_funcionario'] = True
                flash(message, 'success')
                return redirect(url_for('main_page'))
            else:
                flash(message, 'danger')
        return render_template('cadastro.html')

    @app.route('/main')
    def main_page():
        print("Rota /main acessada")
        if 'logged_in' not in session or not session['logged_in']:
            return redirect(url_for('login_page'))
        return render_template('main.html', username=session['username'], is_admin=session.get('is_admin', False))

    @app.route('/logout')
    def logout():
        print("Rota /logout acessada")
        session.pop('logged_in', None)
        session.pop('username', None)
        session.pop('is_admin', None)
        session.pop('funcionario_id', None)
        session.pop('logged_in_funcionario', None)
        return redirect(url_for('login_page'))

    @app.route('/funcionario/incluir', methods=['GET', 'POST'])
    def incluir_funcionario():
        print("Rota /funcionario/incluir acessada")
        if not session.get('is_admin', False):
            flash('Acesso negado!', 'danger')
            return redirect(url_for('main_page'))
        if request.method == 'POST':
            nome = request.form['nome']
            idade = request.form['idade']
            profissao = request.form['profissao']
            rua = request.form['rua']
            cidade = request.form['cidade']
            estado = request.form['estado']
            cep = request.form['cep']
            username = request.form['username']
            password = request.form['password']
            novo_endereco = Endereco(rua=rua, cidade=cidade, estado=estado, cep=cep)
            novo_funcionario = Funcionario(nome=nome, idade=idade, profissao=profissao, username=username, password=password)
            FuncionarioController.Incluir(novo_funcionario, novo_endereco)
            flash('Funcionário incluído com sucesso!', 'success')
            return redirect(url_for('listar_funcionarios'))
        return render_template('funcionario/create.html')

    @app.route('/funcionario/consultar')
    def listar_funcionarios():
        print("Rota /funcionario/consultar acessada")
        if not session.get('is_admin', False):
            return redirect(url_for('ver_perfil'))
        funcionarios = FuncionarioController.SelecionarTodos()
        funcionarios_pontos = {}
        for funcionario in funcionarios:
            funcionarios_pontos[funcionario.id] = FuncionarioController.AgruparPontosPorDiaMes(funcionario.id)
        return render_template('funcionario/list.html', funcionarios=funcionarios, funcionarios_pontos=funcionarios_pontos)

    @app.route('/funcionario/excluir/<id>')
    def excluir_funcionario(id):
        print(f"Rota /funcionario/excluir/{id} acessada")
        if not session.get('is_admin', False):
            flash('Acesso negado!', 'danger')
            return redirect(url_for('main_page'))
        FuncionarioController.Excluir(id)
        flash('Funcionário excluído com sucesso!', 'success')
        return redirect(url_for('listar_funcionarios'))

    @app.route('/funcionario/alterar/<id>', methods=['GET', 'POST'])
    def alterar_funcionario(id):
        print(f"Rota /funcionario/alterar/{id} acessada")
        if not session.get('is_admin', False) and session['funcionario_id'] != id:
            flash('Acesso negado!', 'danger')
            return redirect(url_for('main_page'))
        funcionario = FuncionarioController.SelecionarById(id)
        if not funcionario:
            flash('Funcionário não encontrado!', 'danger')
            return redirect(url_for('main_page'))
        if request.method == 'POST':
            funcionario.nome = request.form['nome']
            funcionario.idade = request.form['idade']
            funcionario.profissao = request.form['profissao']
            funcionario.endereco.rua = request.form['rua']
            funcionario.endereco.cidade = request.form['cidade']
            funcionario.endereco.estado = request.form['estado']
            funcionario.endereco.cep = request.form['cep']
            funcionario.username = request.form['username']
            funcionario.password = request.form['password']
            FuncionarioController.Alterar(funcionario, funcionario.endereco)
            flash('Funcionário alterado com sucesso!', 'success')
            return redirect(url_for('listar_funcionarios') if session.get('is_admin', False) else url_for('ver_perfil'))
        return render_template('funcionario/create.html', funcionario=funcionario)

    @app.route('/funcionario/login', methods=['GET', 'POST'])
    def login_funcionario():
        print("Rota /funcionario/login acessada")
        if request.method == 'POST':
            username = request.form['username']
            password = request.form['password']
            print(f"Tentativa de login de funcionário com usuário: {username}")
            funcionario = FuncionarioController.SelecionarByUsername(username)
            if funcionario and funcionario.password == password:
                session['logged_in_funcionario'] = True
                session['funcionario_id'] = str(funcionario.id)
                flash('Login bem-sucedido!', 'success')
                return redirect(url_for('ponto_funcionario'))
            else:
                flash('Credenciais inválidas', 'danger')
        return render_template('funcionario/login.html')

    @app.route('/funcionario/ponto', methods=['GET', 'POST'])
    def ponto_funcionario():
        print("Rota /funcionario/ponto acessada")
        if 'logged_in_funcionario' not in session or not session['logged_in_funcionario']:
            return redirect(url_for('login_funcionario'))
        funcionario_id = session['funcionario_id']
        pontos = FuncionarioController.SelecionarPontos(funcionario_id)
        if request.method == 'POST':
            if 'registrar_entrada' in request.form:
                FuncionarioController.RegistrarPontoEntrada(funcionario_id)
                flash('Entrada registrada com sucesso!', 'success')
            elif 'registrar_saida' in request.form:
                FuncionarioController.RegistrarPontoSaida(funcionario_id)
                flash('Saída registrada com sucesso!', 'success')
            return redirect(url_for('ponto_funcionario'))
        return render_template('funcionario/ponto.html', pontos=pontos)

    @app.route('/funcionario/perfil')
    def ver_perfil():
        print("Rota /funcionario/perfil acessada")
        if 'logged_in_funcionario' not in session or not session['logged_in_funcionario']:
            return redirect(url_for('login_funcionario'))
        funcionario_id = session['funcionario_id']
        funcionario = FuncionarioController.SelecionarById(funcionario_id)
        if not funcionario:
            flash('Funcionário não encontrado!', 'danger')
            return redirect(url_for('main_page'))
        pontos = FuncionarioController.AgruparPontosPorDiaMes(funcionario_id)
        return render_template('funcionario/perfil.html', funcionario=funcionario, pontos=pontos)