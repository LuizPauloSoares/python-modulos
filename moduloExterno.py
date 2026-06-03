import requests

def requisitar ():
    url = "https://api.github.com"

    parametros = {}

    try:
        response = requests.get(url)
        if response.status_code == 200:
            dados = response.json()

            print(dados)
            

        elif response.status_code == 404:
            print("requisiçao nao encontrada ")

        else:
            print("erro desconhecido tente nocamente")            
        
    except:
        print(f"ocorreu uma exceção: {str(e)}")

requisitar()