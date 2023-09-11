import os
import time

import pandas as pd
import pyautogui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By


def busca_all_click(driver: str, tipo:str, objeto_buscado:str, escrever=None):

    tipos = {
        'css': By.CSS_SELECTOR,
        'name': By.NAME,
        'id': By.ID,
    }
    try:
        time.sleep(3)
        if escrever == None:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((tipos[tipo], objeto_buscado)))
            driver.find_element(tipos[tipo], objeto_buscado).click()
        else:
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((tipos[tipo], objeto_buscado))).click()
            campo = driver.find_element(tipos[tipo], objeto_buscado)
            campo.send_keys(escrever)

    except:
        pass


    finally:

        time.sleep(2)


def escrever(tab:int, escrever:str):

    for i in range(0,tab):
        pyautogui.press('Tab')

    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.write(escrever)

def confirma(tab:int):

    for i in range(0,tab):
        pyautogui.press('Tab')
    pyautogui.press('enter')

    time.sleep(1)

def aa():
    dados = pd.read_excel("C:/tester/atualizar_office_teste.xlsx")

    for i in range(0,len(dados['Nome do colaborador'])):

        espaco = []
        nome = dados['Nome do colaborador'][i]

        for i in range(0,len(nome)):
            if nome[i] == " ":
                espaco.append(i)

        nome_buscado = nome[0:espaco[0]]+nome[espaco[-1]:]
        nome_buscado = nome_buscado.lower()
        print(nome_buscado)


def teste():

    dados = pd.read_excel("C:/tester/atualizar_office_teste.xlsx")

    senha = "Beeh2501"
    navegador = webdriver.Chrome()
    nome_buscado = "Breno"

    gerente = dados['Gestor']

    navegador.get("https://admin.microsoft.com/?auth_upn=breno.sales%40stellaenergia.com.br&source=applauncher#/users")

    busca_all_click(navegador, 'id', 'i0118', senha)
    busca_all_click(navegador, 'id', 'idSIButton9')
    busca_all_click(navegador, 'id', 'idSIButton9')
    busca_all_click(navegador, 'name', 'Usuários')
    busca_all_click(navegador, 'name', 'Usuários ativos')

    try:
        for linha in range(0,len(dados['Nome do colaborador'])):
            if dados['feito'][linha] != 1:

                gerente = dados['Gestor'][linha]
                espaco_gerente = []
                for esp in range(0, len(gerente)):
                    if gerente[esp] == " ":
                        espaco_gerente.append(esp)

                gerente = gerente[0:espaco_gerente[0]] + gerente[espaco_gerente[-1]:]

                espaco = []
                nome = dados['Nome do colaborador'][linha]

                for esp in range(0, len(nome)):
                    if nome[esp] == " ":
                        espaco.append(esp)

                primeiro_nome = nome[0:espaco[0]].title()
                nome_buscado = nome[0:espaco[0]] + nome[espaco[-1]:]
                nome_buscado = nome_buscado.title()

                busca_all_click(navegador, 'css', 'input[role="searchbox"]')
                pyautogui.hotkey('ctrl', 'a')
                pyautogui.press('del')
                escrever(0,nome_buscado)


                pyautogui.press('enter')

                busca_all_click(navegador, 'css', 'div[data-automation-key="DisplayName"]') # vai selecionar sempre o primeiro encontrado na listagem

                time.sleep(10)
                # try:
                #     busca_all_click(navegador, 'css','button[data-automation-id="AlternativeLinkLink"]')  # vai selecionar endereço de email alternativo caso exista
                #     pyautogui.press('tab')
                #     pyautogui.press('tab')
                #     pyautogui.press('del')
                #     pyautogui.press('tab')
                #     pyautogui.press('enter')

                # finally:
                modal = navegador.find_element(By.CSS_SELECTOR, 'div[class^="ms-Panel-scrollableContent scrollableContent-"]')
                busca_all_click(modal, 'css', 'button[arialabel="Adicionar gerenciador"]')
                # confirma(13)
                escrever(2,gerente) # escolher gerente
                time.sleep(3)
                confirma(0) #escolher o primeiro presente na pesquisa
                confirma(1) #salvar alterações
                time.sleep(3)
                pyautogui.press('esc') # voltar a tela do usuario
                pyautogui.press('esc')

                busca_all_click(navegador, 'css','div[data-automation-key="DisplayName"]')  # vai selecionar sempre o primeiro encontrado na listagem

                time.sleep(10)
                confirma(14)
                time.sleep(2)
                for cont in range(0,4):
                    pyautogui.press('tab')
                # escrever(2,'Breno') # nome
                # escrever(1, 'Sales')  # sobrenome
                # escrever(1, nome_buscado+' - Stella Energia')  # nome de exibição
                escrever(1, dados['Cargo'][linha])  # cargo
                # escrever(1, ' ')  # Departamento
                pyautogui.press('tab')
                confirma(10) # confirma
                time.sleep(3)
                confirma(2)  # fecha a edição
                # confirma(5) # clica em fechar
                time.sleep(3)
                pyautogui.press('esc')
                pyautogui.press('esc')
                print(f'feito usuario = {nome_buscado}')

                dados['feito'][linha] = '1'

    finally:
        dados.to_excel("C:/tester/atualizar_office_teste.xlsx", index=False)

    # busca_all_click(navegador, 'css', 'button[humanfriendlyname="EditContactInformation"]')

    os.system("pause")
    print("ok")





    print(dados)

if __name__ == "__main__":
    teste()