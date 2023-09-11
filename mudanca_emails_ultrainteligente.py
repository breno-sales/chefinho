import webbrowser
import time

import pandas as pd
import pyautogui


def inicio():

    webbrowser.open("https://stellaenergia.callix.com.br/login")
    time.sleep(5)
    pyautogui.click(153 , 269)
    pyautogui.click(163 , 321)
    time.sleep(1)
    pyautogui.click(166 , 362)
    time.sleep(2)

    repeticao()

def repeticao():

    dados = pd.read_excel("C:/tester/mudanca.xlsx")

    for i in range(0,len(dados['Nome UPN'])):

        email = dados['Nome UPN'][i]

        email = email[0:email.find('@')]
        nome_todo = email[0:email.find('.')]+" "+email[email.find('.')+1:] #+" - Ultragaz Energia Inteligente"
        nome_todo = nome_todo.title()

        pyautogui.click(1615 , 362) # clica na barra de pesquisa
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('del')
        pyautogui.write(email)
        pyautogui.press('enter')
        time.sleep(5)
        pyautogui.click(629 , 510) # seleciona o usuario
        time.sleep(5)
        pyautogui.click(1322 , 600) # gerenciar nome de usuario e email
        time.sleep(1)
        pyautogui.click(1850 , 558) # lapis/edicao
        time.sleep(1)
        pyautogui.click(1604 , 594) # clica no dominio
        time.sleep(1)
        pyautogui.click(1350 , 990) # seleciona o ultragazenergiainteligente
        time.sleep(1)
        pyautogui.click(1795 , 593) # concluido
        time.sleep(3)
        pyautogui.click(1310 , 987) # salvar
        time.sleep(10)
        pyautogui.click(1883 , 230) # fecha o card do usuario
        time.sleep(1)

        pyautogui.click(629, 510)  # seleciona o usuario
        time.sleep(5)
        pyautogui.click(1154 , 368)  # clica nos 3 pontos
        time.sleep(2)
        pyautogui.click(1262 , 682)  # gerenciar informaçoes de contato
        time.sleep(2)
        pyautogui.click(1481 , 600)  # clica nao nome de exibição
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('del')
        pyautogui.write(nome_todo)
        pyautogui.click(1330 , 980) # salvar
        time.sleep(2)
        pyautogui.click(1883, 230)  # fecha o card do usuario
        time.sleep(1)

        print(f" alterado email de: {nome_todo}")





if __name__ == "__main__":
    inicio()