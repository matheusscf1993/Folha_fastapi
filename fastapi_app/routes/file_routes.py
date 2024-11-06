from fastapi import APIRouter, HTTPException
from datetime import datetime
from domain.file_processor import FileProcessor

router = APIRouter()

# Criar uma instância do FileProcessor para manipulação de dados no arquivo CSV
file_processor = FileProcessor()

@router.get("/consultar_pontos/")
async def consultar_pontos():
    """ Consulta todos os registros de ponto e envia para o Flask. """
    try:
        # Lista todos os dados do CSV
        data = await file_processor.list_data()

        # Envia todos os dados do CSV para o Flask
        await file_processor.api_client.send_all_data(data)

        return data  # Retorna os dados processados
    except HTTPException as e:
        raise e
