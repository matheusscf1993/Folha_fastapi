from fastapi import FastAPI
from routes import init_routes  # Importa a função que registra as rotas

app = FastAPI()

# Inicializa as rotas
init_routes(app)

@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao sistema de folha de ponto!"}
