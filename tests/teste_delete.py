import requests

headers = {'AUthorization': 'Token 099cd66b13f62cb698873b7c7442c4ab821a2823'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.delete(url=f'{url_base_cursos}6/', headers=headers)

# Testando o código HTTP
assert resultado.status_code == 204

# print(resultado.txt)

# Testando se o tamanho do conteudo retornado é 0
assert len(resultado.text) == 0