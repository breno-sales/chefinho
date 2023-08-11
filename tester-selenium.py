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

    if escrever != None:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((tipos[tipo], objeto_buscado))).click()
        campo = driver.find_element(tipos[tipo], objeto_buscado)
        campo.send_keys(escrever)

    else:
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((tipos[tipo], objeto_buscado))).click()

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

        nome = dados['Nome do colaborador'][i]
        espaco = nome.find(' ')
        nome_buscado = nome[0:espaco[0]]+' '+nome[espaco[-1]:]
        print(nome_buscado)

def teste():

    dados = pd.read_excel("C:/tester/atualizar_office_teste.xlsx")

    senha = "Beeh2501"
    navegador = webdriver.Chrome()
    nome_buscado = "Breno"

    navegador.get("https://admin.microsoft.com/?auth_upn=breno.sales%40stellaenergia.com.br&source=applauncher#/users")

    busca_all_click(navegador, 'id', 'i0118', senha)
    busca_all_click(navegador, 'id', 'idSIButton9')
    busca_all_click(navegador, 'id', 'idSIButton9')
    busca_all_click(navegador, 'name', 'Usuários')
    busca_all_click(navegador, 'name', 'Usuários ativos')

    for i in range(0,dados['Nome do colaborador']):

        nome = dados['Nome do colaborador'][i]
        nome_buscado = nome[0:nome.find(' ')[0]]+' '+nome[nome.find(' ')[-1]:]
        print(nome_buscado)

    busca_all_click(navegador, 'css', 'input[role="searchbox"]', nome_buscado)
    pyautogui.press('enter')

    busca_all_click(navegador, 'css', 'div[data-automation-key="DisplayName"]') # vai selecionar sempre o primeiro encontrado na listagem

    time.sleep(3)
    confirma(14)

    time.sleep(2)

    escrever(2,'Breno') # nome
    escrever(1, 'Sales')  # sobrenome
    escrever(1, nome_buscado+' - Stella Energia')  # nome de exibição
    escrever(1, 'Beeh')  # cargo
    escrever(1, 'Beeh')  # Departamento
    confirma(10) # confirma
    confirma(2)  # fecha a edição
    confirma(5) # clica em fechar


    # busca_all_click(navegador, 'css', 'button[humanfriendlyname="EditContactInformation"]')

    os.system("pause")
    print("ok")



if __name__ == "__main__":
    aa()