from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Rota Raiz

@app.get('/')
def raiz():
    return {'Olá': 'Mundo'}

# Criar model

class Usuario(BaseModel):
    id : int
    email : str
    senha : str

# Criar base de dados

base_de_dados = [
    Usuario(id=1, email='matheus.arimura@gmail.com', senha='12345'),
    Usuario(id=2, email='pedroarimura@gmail.com', senha='12345'),
]

# Rota Get All

@app.get('/usuarios')
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get ID

@app.get('/usuarios/{id_usuario}')
def get_usuario_usando_id(id_usuario : int):
    for usuario in base_de_dados:
        if (usuario.id == id_usuario):
            return usuario
        
    return {'Status' : 404, 'Mensagem' : 'Usuário não encontrado.'}

# Rota Insere

@app.post('/usuarios')
def insere_usuario(usuario : Usuario):
    # Criar regras de negocio   
    for registro in base_de_dados:
        if (registro.id == usuario.id or registro.email == usuario.email):
            return {'Status' : 409, 'Mensagem' : 'Identificador já existente.'}

    base_de_dados.append(usuario)
    return usuario
