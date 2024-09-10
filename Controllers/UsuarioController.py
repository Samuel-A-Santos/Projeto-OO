from models.Usuario import Usuario
from models.Funcionario import Funcionario
from models.Endereco import Endereco
from werkzeug.security import generate_password_hash, check_password_hash

def cadastrar_usuario(nome, idade, profissao, rua, cidade, estado, cep, username, password):
    if Usuario.objects(username=username).first():
        return False, "Usuário já existe"
    hashed_password = generate_password_hash(password)
    usuario = Usuario(username=username, password=hashed_password)
    usuario.save()

    endereco = Endereco(rua=rua, cidade=cidade, estado=estado, cep=cep)
    funcionario = Funcionario(nome=nome, idade=idade, profissao=profissao, endereco=endereco, username=username, password=hashed_password)
    funcionario.save()

    return True, "Usuário cadastrado com sucesso"

def login_usuario(username, password):
    usuario = Usuario.objects(username=username).first()
    if not usuario or not check_password_hash(usuario.password, password):
        return False, "Credenciais inválidas"
    return True, "Login bem-sucedido"

def logout_usuario():
    pass

def SelecionarTodos():
    return Usuario.objects()

def is_admin(username):
    return username == "samuel20"