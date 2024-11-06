import csv
import os
from fastapi import HTTPException, status
from services.api_client import APIClient
from datetime import datetime

class FileProcessor:

    def __init__(self):
        self.file_path = 'data/folha_de_ponto.csv'  # Caminho para o arquivo de dados
        self.directory = 'data'
        self.api_client = APIClient()

    async def list_data(self):
        """ Lista todos os registros de ponto no arquivo CSV e envia para o APIClient. """
        if os.path.exists(self.file_path):
            with open(self.file_path, mode='r') as file:
                csv_reader = csv.reader(file)
                next(csv_reader)  # Pular o cabeçalho
                for row in csv_reader:
                    row_dict = {
                        "funcionario_id": row[0],
                        "data": row[1],
                        "hora_entrada": row[2],
                        "hora_saida": row[3]
                    }
                    await self.api_client.send_data(row_dict)  # Envia os dados para o serviço API
            return {"detail": "Arquivo de ponto processado com sucesso!"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Arquivo de ponto inexistente!")

    def create_file(self):
        """ Cria o arquivo CSV caso não exista. """
        if not os.path.exists(self.file_path):
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['funcionario_id', 'data', 'hora_entrada', 'hora_saida'])  # Cabeçalho
            return {"mensagem": f"Arquivo {self.file_path} criado com sucesso."}
        else:
            raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                detail="Arquivo de ponto já existe")

    async def add_data_to_file(self, data: dict):
        """ Adiciona um registro de ponto ao arquivo CSV. """
        if os.path.exists(self.file_path):
            with open(self.file_path, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([data["funcionario_id"], data["data"], data.get("hora_entrada", ""), data.get("hora_saida", "")])
                return {"mensagem": f"Registro de ponto inserido com sucesso: {data}"}
        else:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail="Arquivo de ponto inexistente, por favor acessar"
                                       " a rota de criar o arquivo.")
