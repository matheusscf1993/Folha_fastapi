from datetime import datetime

# Função já existente para converter valores monetários (R$) para float
def real_to_float(real: str) -> float:
    try:
        real = real.replace('R$', '')  # Remove o símbolo "R$"
        real = real.replace('.', '')   # Remove os pontos de milhar
        real = real.replace(' ', '')   # Remove espaços em branco
        real = real.replace(',', '.')  # Substitui a vírgula por ponto
        return float(real)
    except Exception as e:
        raise ValueError(f"Erro ao converter valor: {e}")


# Função para formatar uma data no formato 'dd/mm/yyyy' para 'yyyy-mm-dd'
def format_date(date_str: str) -> str:
    try:
        # Converte a string de data para o formato 'YYYY-MM-DD'
        date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        return date_obj.strftime('%Y-%m-%d')
    except ValueError:
        raise ValueError("Formato de data inválido. Use o formato dd/mm/yyyy.")


# Função para calcular o total de horas trabalhadas, dado o horário de entrada e saída
def calcular_horas_trabalhadas(hora_entrada: str, hora_saida: str) -> float:
    try:
        # Define o formato das horas
        formato = "%H:%M"
        
        # Converte as horas de entrada e saída para objetos datetime
        entrada = datetime.strptime(hora_entrada, formato)
        saida = datetime.strptime(hora_saida, formato)
        
        # Calcula a diferença em horas e retorna como float
        delta = saida - entrada
        return delta.seconds / 3600.0  # Converte de segundos para horas
    except ValueError:
        raise ValueError("Formato de hora inválido. Use o formato HH:MM.")


# Função para gerar um ID único para cada transação (opcional, caso queira acompanhar registros)
def gerar_id_unico() -> str:
    # Gera um ID único baseado no timestamp atual
    return datetime.now().strftime('%Y%m%d%H%M%S')
