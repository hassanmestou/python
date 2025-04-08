url = "http://www.pudim.com.br"

try:
    response = requests.get(url)
    if response.status_code == 200:
        print("Site online")
    else:
        print("Site offline")
except requests.exceptions.RequestException as e:
    print("Problema na conexão", e)
except ModuleNotFoundError as erro:
    print("Problema no modulo importado", erro.__class__)



