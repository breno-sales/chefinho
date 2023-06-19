import pyautogui
import time
import webbrowser
import pandas as pd

def abrir_site():
    # x, y = pyautogui.position()
    # print(x,y)
    login = "brenosales"
    senha = "Stella123!"

    webbrowser.open("https://stellaenergia.callix.com.br/login")
    time.sleep(5)
    pyautogui.click(1153,520)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.write(login)
    pyautogui.press('tab')
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('del')
    pyautogui.write(senha)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(10)
    pyautogui.moveTo(1131,160)
    time.sleep(1)
    pyautogui.click(1131,231)
    time.sleep(3)

def criar_usuario():

    dados = pd.read_excel("C:/tester/tester.xlsx")

    for i in range(0, len(dados["nome_colaborador"])):

        nome = str(dados["name"][i])
        email = str(dados["email"][i])
        login = nome.replace(" ",".")
        login = login.lower()
        senha = str(dados["password"][i])

        pyautogui.click(1776,287)
        time.sleep(3)
        pyautogui.click(674,467)
        time.sleep(1)
        pyautogui.write(nome)
        pyautogui.press('tab')
        pyautogui.write(email)
        time.sleep(1)
        pyautogui.press('tab')
        pyautogui.press('tab')
        pyautogui.write(login)
        time.sleep(1)
        pyautogui.click(883,538) #abrir perfil de acesso
        time.sleep(1)
        pyautogui.click(645,597) #escolher perfil de agente
        time.sleep(1)
        pyautogui.click(733,834)  # abrir menu equipe
        time.sleep(1)
        pyautogui.click(630,588)  # selecionar equipe
        time.sleep(1)
        pyautogui.click(1819,965) #salvar
        time.sleep(5)
#------------------definir senha -------------
        pyautogui.click(168,364)
        pyautogui.write(login)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(1)
        pyautogui.click(1842,484)
        pyautogui.click(1737,484)
        time.sleep(1)
        pyautogui.click(911,524)
        pyautogui.write(senha)
        pyautogui.press('tab')
        pyautogui.write(senha)
        pyautogui.press('tab')
        pyautogui.press('enter')
        time.sleep(3)



if __name__ == '__main__':
    abrir_site()
    criar_usuario()