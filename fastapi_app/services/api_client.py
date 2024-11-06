import requests
from settings.config import Config  # Importando configurações da URL da API

class APIClient:
    def __init__(self):
        """ Inicializa o cliente da API com a URL configurada. """
        self.api_url = Config.FLASK_API_URL  # A URL da API onde os dados serão enviados

    def send_data(self, data):
        """ Envia os dados do ponto para o servidor Flask via POST. """
        try:
            # Faz a requisição POST enviando os dados como JSON
            response = requests.post(self.api_url, json=data)
            
            # Verifica se a resposta da API foi bem-sucedida
            response.raise_for_status()
            
            return {"message": "Dados enviados com sucesso!", "status": response.status_code}
        
        except requests.exceptions.RequestException as e:
            # Se houver erro na requisição, levanta uma exceção com uma mensagem detalhada
            raise Exception(f"Erro ao enviar dados: {e}")

    # Método para enviar todos os dados do arquivo para o Flask
    async def send_all_data(self, data_list):
        for data in data_list:
            response = self.send_data(data)  # Envia cada ponto individualmente
            if response["status"] != 200:
                raise HTTPException(status_code=response["status"], detail="Erro ao enviar dados ao Flask.")
        return {"detail": "Todos os dados foram enviados com sucesso."}
