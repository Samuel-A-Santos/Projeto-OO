from models.Usuario import Usuario
from models.Funcionario import Funcionario
from models.Endereco import Endereco
from werkzeug.security import generate_password_hash, check_password_hash

def cadastrar_usuario(nome, idade, profissao, rua, cidade, estado, cep, username, password):
    print(f"Verificando se o usuário {username} já existe...")
    if Usuario.objects(username=username).first():
        print("Usuário já existe.")
        return False, "Usuário já existe"
    hashed_password = generate_password_hash(password)
    usuario = Usuario(username=username, password=hashed_password)
    usuario.save()
    print(f"Usuário {username} cadastrado com sucesso.")

    endereco = Endereco(rua=rua, cidade=cidade, estado=estado, cep=cep)
    funcionario = Funcionario(nome=nome, idade=idade, profissao=profissao, endereco=endereco, username=username, password=hashed_password)
    funcionario.save()
    print(f"Funcionário {username} cadastrado com sucesso.")

    return True, "Usuário cadastrado com sucesso"

def login_usuario(username, password):
    print(f"Tentando fazer login com o usuário {username}...")
    usuario = Usuario.objects(username=username).first()
    if not usuario or not check_password_hash(usuario.password, password):
        print("Credenciais inválidas.")
        return False, "Credenciais inválidas"
    print("Login bem-sucedido.")
    return True, "Login bem-sucedido"

def logout_usuario():
    pass

def SelecionarTodos():
    return Usuario.objects()

def is_admin(username):
    return username == "samuel20"