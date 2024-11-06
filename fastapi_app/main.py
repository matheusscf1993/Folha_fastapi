import uvicorn
from fastapi import FastAPI
from routes.file_routes import router as file_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Sistema de Folha de Ponto - Bem-vindo"}

app.include_router(file_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
