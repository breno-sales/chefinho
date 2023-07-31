import pandas as pd
import win32com.client as win32


def enviar_email(mensagem: str, email_para_envio: str):

    olApp = win32.Dispatch('Outlook.Application')
    olNS = olApp.GetNameSpace('MAPI')

    # construct email item object
    mailItem = olApp.CreateItem(0)
    mailItem.Subject = 'Boas Vindas a Stella Energia' #titulo
    mailItem.BodyFormat = 1
    mailItem.Body = mensagem # corpo da mensagem
    mailItem.To = email_para_envio # para
    mailItem.Sensitivity  = 2

    # mailItem.Display()

    mailItem.Send()


def dados():
    dados = pd.read_excel("C:/tester/tester.xlsx")

    for i in range(0, len(dados['email'])):

        nome_colaborado = dados['nome_colaborador'][i]

        nome_usuario = dados['name'][i].lower()
        nome_usuario = nome_usuario.replace(" ", ".")

        email = dados['email'][i]

        senha_padrao = nome_usuario[0].upper()
        senha_padrao += nome_usuario[nome_usuario.find(".")+1].upper()

        mensagem = f"""Prezados {nome_colaborado}, Bom dia.
    
        Seja muito bem-vindo a Stella Energia,
        
        Sou Breno Sales, membro da equipe de TI, estou aqui para dar apoio e suporte a qualquer questão de acessos e apoio tecnológico, sempre que precisar, estarei a disposição para ajudar, pode estar me chamando através do slack, e/ou teams.
        
        Acessos:
        
        Chatguru:
        Login: {email}
        Senha: Stella123!
        
        Callix:
        Login: {nome_usuario}
        Senha: Stella123!
        
        Email/Teams:
        Login: {email}
        Senha: {senha_padrao}#@!1310"""

        enviar_email(mensagem=mensagem, email_para_envio=email)
        print(f'email enviado para {nome_colaborado}')

if __name__ == '__main__':
    dados()