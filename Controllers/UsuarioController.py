from models.Usuario import Usuario
from werkzeug.security import generate_password_hash, check_password_hash

def cadastrar_usuario(username, password):
    if Usuario.objects(username=username).first():
        return False, "Usuário já existe"
    hashed_password = generate_password_hash(password)
    usuario = Usuario(username=username, password=hashed_password)
    usuario.save()
    return True, "Usuário cadastrado com sucesso"

def login_usuario(username, password):
    usuario = Usuario.objects(username=username).first()
    if not usuario or not check_password_hash(usuario.password, password):
        return False, "Credenciais inválidas"
    return True, "Login bem-sucedido"

def logout_usuario():
    # Implementar lógica de logout se necessário
    pass

def SelecionarTodos():
    return Usuario.objects()