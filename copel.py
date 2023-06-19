import json
import webbrowser
import time
import pandas
import pyautogui
import requests as requests

n_pages = 12

def abrir_site():
    # x, y = pyautogui.position()
    # print(x,y)
    webbrowser.open("https://app.solarz.com.br/login?logout")
    time.sleep(5)
    pyautogui.click(598,725)
    time.sleep(3)
    pyautogui.click(32,277)
    time.sleep(3)
    pyautogui.click(1118,444)

def executar(uc: str, cpf_cnpj: str,senha: str,tipo: str):

    pyautogui.write(uc) # pesquisar a uc encontrada
    pyautogui.press('enter')
    time.sleep(3)
    pyautogui.click(227,556) # clicar na uc
    time.sleep(2)

    if tipo == 'Residências' or tipo == 'Edifícios / condomínios residenciais':
        pyautogui.click(1290,531) # seleciona a tag casa
    else:
        pyautogui.click(1609,527) # seleciona a tag 'empresa baixa tensao'

    time.sleep(2)
    pyautogui.click(1462,635) # clicar e preencher cpf/cnpj da uc
    pyautogui.write(cpf_cnpj)
    time.sleep(1)
    pyautogui.click(1673,724)  # clicar e preencher senha da uc
    for i in range(0,30):
        pyautogui.press('Backspace')

    pyautogui.write(senha)
    time.sleep(1)
    pyautogui.click(1459,783) # clicar em salvar
    time.sleep(6)
    pyautogui.click(32,280) # apos carregar pagina em sucesso, voltar para a pagina de pesquisa
    time.sleep(5)
    pyautogui.click(1118, 444) # clicar na pesquisa esperando por novo match


def get_cookies():

    login_solarz = 'financeiro@stellaenergia.com.br'
    psswd_solarz = 'Stella2022!'

    url = 'https://app.solarz.com.br/login'
    data = {
        'username': login_solarz,
        'password': psswd_solarz,
    }
    session = requests.Session()
    session.post(url, data)
    return session

def get_dados(n_pages,session=None): # retorna os htmls de cada pagina

    if session is None:
        session = get_cookies()

    htmls = []

    data_pesquisa = '&mesAno=2022-12-31'
    for page in range(0,n_pages):
        url = f'https://app.solarz.com.br/integrador/faturas/list?page={page}&query={data_pesquisa}&faturaStatusFilter=notInformed&concessionariaFilter=102'
        res = session.get(url=url)
        res = res.text
        htmls.append(res)


    return htmls

def leitura_cards_por_pages(data_solarz:list): #retorna as ucs de cada pagina

    resp = []
    for page in range(0,len(data_solarz)):
        pagina = data_solarz[page]
        pagina = pagina.split('fa-barcode"></i>')

        ucs_in_page = []
        for i in pagina:
            i = i.strip(' \n')
            i = i[0:15]
            i = i.split(' ')

            if i[0].find('</span>') == -1 and i[0].find('div') == -1:
                # print('---------------------------------------------')
                # print(i[0])
                ucs_in_page.append(i[0])
        resp.append(ucs_in_page)

    return resp


def get_csv():

    conteudo = pandas.read_excel('C:/t1/lista_ucs_copel.xlsx')
    data = conteudo.to_json(orient = 'values')
    data_json = json.loads(data) # retorna do formato [["UC","nome","cpf"],.....]

    return data_json

def match(data_solarz: list, data_csv: list, encontrado=False):

    fazer = []

    for proposta in data_csv:
        encontrado = False
        for uc_in_page in data_solarz:
            for uc in uc_in_page:
                if str(uc) == str(proposta[0]):
                    #mexer aqui
                    print(f'UC {proposta[0]} ENCONTRADA -------------------------------------------------------------------------------')
                    encontrado = True
                    print('executando...')
                    executar(str(uc),str(proposta[1]),str(proposta[2]),str(proposta[3]))
                    print('executado')
                    fazer.append(proposta[0])

        if encontrado == False:
            print(f'UC {proposta[0]} nao encontrada')

    return fazer


if __name__ == '__main__':

    abrir_site()
    data_solarz = get_dados(n_pages) # retorna os htmls de cada pagina
    data_solarz = leitura_cards_por_pages(data_solarz) # retorna as ucs de cada pagina
    dados = get_csv()
    x = match(data_solarz, dados)
    print(x)
