import requests

API_KEY = "b31fedb141f4a82c5df899de29973349"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(cidade: str):
    """Consulta a API do OpenWeatherMap e retorna o clima atual da cidade"""
    params = {
        "q": f"{cidade},BR",
        "appid": API_KEY,
        "units": "metric",
        "lang": "pt_br"
    }
    resposta = requests.get(BASE_URL, params=params)
    
    if resposta.status_code == 200:
        return resposta.json()
    else:
        return {"erro": "Não foi possível obter os dados climáticos"}
