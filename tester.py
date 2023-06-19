import urllib.request
import requests
import re
from bs4 import BeautifulSoup

def get_cookies():

    login = 'breno.sales@stellaenergia.com.br'
    senha = 'Stella123!'

    url = 'https://app4.zap.guru/login'
    data = {
        'email': login,
        'password': senha,
    }
    session = requests.Session()
    session.post(url, data)
    return session
# if __name__ == '__main__':
#    cookies = get_cookies()
#    print(cookies)


def get_dados(session=None): # retorna os htmls de cada pagina

    if session is None:
        session = get_cookies()

    htmls = []

    # data_pesquisa = '&mesAno=2022-12-31'
    # for page in range(0,n_pages):
    #     url = f'https://app.solarz.com.br/integrador/faturas/list?page={page}&query={data_pesquisa}&faturaStatusFilter=notInformed&concessionariaFilter=102'
    #     res = session.get(url=url)
    #     res = res.text
    #     htmls.append(res)

    url = 'https://app4.zap.guru/reports/accesses/generate/1'

    data_inicio = '2022-12-19'
    data_fim = '2022-12-25'
    json = {
        'users_ids': '629bcdfc4901a27c7e298dce',
        'created_from': str(data_inicio),
        'created_to': str(data_fim)
    }
    res = session.post(url=url,data=json)
    print(res.text)


    return res



def regex_data(texto:str):

    expression = re.compile('[<][t][d][>][0-9]{4}[-][0-9]{2}[-][0-9]{2}') # data completa no html
    data = re.compile('[0-9]{4}[-][0-9]{2}[-][0-9]{2}') # data dentro dos match no html
    matchs = re.findall(expression,texto.text) # acha todas as ocorrencias.
    print(matchs)

    for i in matchs:
        x = re.findall(data,i)
        print(x)

def regex_horario(texto:str):

    horas_entrada = re.compile('[0-9]{2}[:][0-9]{2}[:][0-9]{2}[<][/][t][d][>]') # data completa no html
    horas_saida = re.compile('<td>[0-9]{2}[:][0-9]{2}[:][0-9]{2}</td>')  # data completa no html
    horas = re.compile('[0-9]{4}[-][0-9]{2}[-][0-9]{2}') # data dentro dos match no html
    matchs_entrada = re.findall(horas_entrada,texto.text) # acha todas as ocorrencias.
    matchs_saida = re.findall(horas_saida, texto.text)  # acha todas as ocorrencias.
    print(f'entrada: {matchs_entrada}\nsaida: {matchs_saida}\n\n')

    # for i in matchs:
    #     x = re.findall(horas,i)
    #     print(x)


if __name__ == '__main__':
    dados = get_dados()
    # regex_data(dados)
    regex_horario(dados)