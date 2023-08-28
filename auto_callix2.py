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

def busca_campos_repetidos(driver: str, tipo:str, objeto_buscado:str, escrever=None, repeticao=None):

    tipos = {
        'css': By.CSS_SELECTOR,
        'name': By.NAME,
        'id': By.ID,
    }

    if repeticao != None:
        campo = driver.find_elements(tipos[tipo], objeto_buscado)
        campo[repeticao].click()

    time.sleep(2)

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


def criar_user_callix():

    dados = pd.read_excel("C:/tester/tester.xlsx")

    login = "brenosales"
    senha = "Stella123!"
    navegador = webdriver.Chrome()
    nome_buscado = "Breno"

    navegador.get("https://stellaenergia.callix.com.br/login")

    busca_all_click(navegador, 'css', 'input[placeholder="Login"]', login)
    busca_all_click(navegador, 'css', 'input[placeholder="Senha"]', senha)
    busca_all_click(navegador, 'css', 'button[data-cy="authenticate"]')
    time.sleep(1)
    pyautogui.press('f11')
    busca_all_click(navegador, 'css', 'a[title="Configurações"]')
    time.sleep(1)
    busca_all_click(navegador, 'css', 'a[title="Usuários"]')
    busca_all_click(navegador, 'css', 'input[placeholder="Buscar"]')

    for i in range(0,len(dados["nome_colaborador"])):
        nome_buscado = dados["nome_colaborador"][i]
        nome_user = str(dados["name"][i])
        email_user = str(dados["email"][i])
        login_user = nome_user.replace(" ", ".")
        login_user = login_user.lower()
        senha_user = str(dados["password"][i])

        busca_all_click(navegador, 'css', 'a[nav-to="users-new"]')
        time.sleep(3)

        pyautogui.press('tab')
        pyautogui.press('tab')
        time.sleep(1)
        pyautogui.write(nome_user)
        pyautogui.press('tab')
        pyautogui.write(email_user)
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(login_user)
        time.sleep(1)
        busca_all_click(navegador, 'css', 'span[tabindex="-1"]') # acesso perfil de acesso
        pyautogui.press('down')
        pyautogui.press('enter')
        busca_campos_repetidos(navegador, 'css', 'span[tabindex="-1"]',repeticao=1)
        pyautogui.press('enter')

        busca_all_click(navegador, 'css', 'button[class="au-target btn solid-success clx-button__button"]')
        time.sleep(3)

        busca_all_click(navegador, 'css', 'input[placeholder="Buscar"]', nome_user)
        pyautogui.press('enter')
        time.sleep(2)
        busca_all_click(navegador, 'css', 'clx-button[class="row-actions au-target"]')
        time.sleep(1)
        pyautogui.click(1734 , 420)
        time.sleep(1)
        pyautogui.click(932 , 520)
        pyautogui.write(senha_user)
        pyautogui.press('tab')
        pyautogui.write(senha_user)
        pyautogui.click(1070 , 698)



if __name__ == "__main__":
    criar_user_callix()