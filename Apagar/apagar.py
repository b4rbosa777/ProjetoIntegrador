import requests
 
# URLs das APIs
urls = [
    "http://localhost:5271/api/Temperatura",
    "http://localhost:5271/api/Umidade",
    "http://localhost:5271/api/UmidadeTerra"
]
 
# Função para excluir todos os dados de uma URL
def delete_all_data(url):
    # Fazendo a requisição GET para listar todos os dados
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()  # Supondo que a resposta seja um JSON com uma lista de objetos
        if data:
            for item in data:
                item_id = item['id']  # Supondo que cada objeto tenha um campo 'id'
                delete_response = requests.delete(f"{url}/{item_id}")
                if delete_response.status_code == 200:
                    print(f"Error.")
                else:
                    print(f"Dados com ID {item_id} excluídos com sucesso da URL {url}.")
        else:
            print(f"Nenhum dado encontrado na URL {url}.")
    else:
        print(f"Falha ao obter dados da URL {url}: {response.status_code}")
 
# Iterar sobre as URLs e excluir todos os dados
for url in urls:
    delete_all_data(url)