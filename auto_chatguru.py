import pandas
import pandas as pd
import requests

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


def dados_excel():

    dados = pd.read_excel("C:/tester/tester.xlsx")

    usuarios_json = []

    for i in range(0,len(dados["nome_colaborador"])):
        linha = []

        linha.append(dados["nome_colaborador"][i])
        linha.append(dados["email"][i])
        linha.append(dados["name"][i])
        linha.append(dados["password"][i])
        linha.append(dados["auto_display_name_text"][i])
        linha.append(dados["type"][i])

        usuarios_json.append(linha)


    return usuarios_json

def dados_excel_update(path: str):

    dados = pd.read_excel(path)

    usuarios_json = []

    for i in range(0,len(dados["auto_display_name_text"])):
        linha = []

        linha.append(dados["auto_display_name_text"][i])
        linha.append(dados["ID"][i])
        linha.append(dados["type"][i])


        usuarios_json.append(linha)
    # print(usuarios_json)


    return usuarios_json


def criar_user_chatguru(session=None): # retorna os htmls de cada pagina

    if session is None:
        session = get_cookies()

    # dados = dados_excel()
    dados = pd.read_excel("C:/tester/tester.xlsx")
    url = 'https://app4.zap.guru/users/add'

    for i in range(0,len(dados["nome_colaborador"])):
        print(dados["email"][i])

        json = {
            "email": str(dados["email"][i]),
            "name": str(dados["name"][i]),
            "password": str(dados["password"][i]),
            "auto_display_name_text": str(dados["auto_display_name_text"][i]),
            "auto_display_name": "on",
            "type": str(dados["type"][i]),
            "permissions": {"ATTACHMENT_SEND",
                            "MSG_SCHEDULE",
                            "CONTACT_ADD",
                            "CONTACT_VIEW",
                            "MSG_RELOAD",
                            "MSG_RELOAD_ALL",
                            "CHATBOT_DIALOG_EXECUTE",
                            "CHAT_FILTER_BY_USER",
                            "CHAT_FILTER_BY_NAME",
                            "CHAT_FILTER_BY_NUMBER",
                            "CHAT_FILTER_BY_PHONE",
                            "CHAT_FILTER_BY_TAG",
                            "CHAT_FILTER_BY_ARCHIVED",
                            "CHAT_FILTER_BY_BROADCAST",
                            "CHAT_FILTER_BY_UNREAD",
                            "CHAT_FILTER_BY_FAVORITED",
                            "CHAT_DELEGATE",
                            "CHAT_CHANGE_NAME",
                            "NOTES_VIEW",
                            "NOTES_ADD",
                            "CHAT_SEE_ALL",
                            "CHAT_VIEW_NUMBER",
                            "CHAT_MARK_UNREAD",
                            "CHAT_MARK_READ",
                            "CHAT_RELOAD_CHATS",
                            "CHAT_ADD_CHAT",
                            "CHAT_DELEGATION_LOGS",
                            "CHAT_VIEW_GROUP_CHATS",
                            "CUSTOM_FIELD_VIEW"
                            }
        }

        response = session.post(url=url,data=json)

        if response.status_code == 200:
            print(f"Criado usuario : {dados['name'][i]}")
        else:
            print(f"ERROR usuario : {dados['name'][i]}")




def update_user(path: str,session=None):

    if session is None:
        session = get_cookies()

    dados = dados_excel_update(path)
    # print(len(dados))
    # print(dados[0])

    for linha in dados:

        ID = linha[1]
        # print(f"{linha} = {ID}")

        url = f'https://app4.zap.guru/users/edit/{ID}/5f3ffc8870ef6413fdec0876'

        # permissions analistas------------------
        permissions_analistas = {
                                "TAG_ADD_TO_CHAT",
                                "TAG_DELETE_TO_CHAT",
                                "USER_ADD_TO_CHAT",
                                "ATTACHMENT_SEND",
                                "CONTACT_ADD",
                                "CONTACT_VIEW",
                                "MSG_SCHEDULE",
                                "MSG_RELOAD",
                                "MSG_RELOAD_ALL",
                                "REPORT_NOTES",
                                "REPORT_ACCESS",
                                "REPORT_STARTCHAT_VIEW",
                                "REPORT_GRAPHICS_VIEW",
                                "REPORT_VIEW",
                                "REPORT_ADD",
                                "REPORT_EXPORT",
                                "REPORT_MSG_VIEW",
                                "REPORT_DIALOG_EXECUTED_VIEW",
                                "CHATBOT_DIALOG_EXECUTE",
                                "CHATBOT_MESSAGE_INFO",
                                "CHATBOT_REPROCESS_MESSAGE",
                                "CHATBOT_APPROVE",
                                "CHATBOT_CONTEXT",
                                "CHAT_FILTER_BY_USER",
                                "CHAT_FILTER_BY_NAME",
                                "CHAT_FILTER_BY_NUMBER",
                                "CHAT_FILTER_BY_PHONE",
                                "CHAT_FILTER_BY_TAG",
                                "CHAT_FILTER_BY_ARCHIVED",
                                "CHAT_FILTER_BY_BROADCAST",
                                "CHAT_FILTER_BY_UNREAD",
                                "CHAT_FILTER_BY_FAVORITED",
                                "CHAT_DELEGATE",
                                "CHAT_CHANGE_NAME",
                                "NOTES_VIEW",
                                "NOTES_ADD",
                                "NOTES_DELETE_OWN",
                                "NOTES_DELETE_ALL",
                                "CHAT_SEE_ALL",
                                "CHAT_VIEW_NUMBER",
                                "CHAT_MARK_UNREAD",
                                "CHAT_MARK_READ",
                                "CHAT_RELOAD_CHATS",
                                "CHAT_RELOAD_PROFILE_PICTURE",
                                "CHAT_ADD_CHAT",
                                "CHAT_DELEGATION_LOGS",
                                "CHAT_VIEW_GROUP_CHATS",
                                "CUSTOM_FIELD_VIEW"}
        # ------------------------------------------
        # permissions operador ------------------------
        permissions_operador = {
                                "TAG_ADD_TO_CHAT",
                                "TAG_DELETE_TO_CHAT",
                                "ATTACHMENT_SEND",
                                "MSG_SCHEDULE",
                                "CONTACT_ADD",
                                "CONTACT_VIEW",
                                "MSG_RELOAD",
                                "MSG_RELOAD_ALL",
                                "CHATBOT_DIALOG_EXECUTE",
                                "CHAT_FILTER_BY_USER",
                                "CHAT_FILTER_BY_NAME",
                                "CHAT_FILTER_BY_NUMBER",
                                "CHAT_FILTER_BY_PHONE",
                                "CHAT_FILTER_BY_TAG",
                                "CHAT_FILTER_BY_ARCHIVED",
                                "CHAT_FILTER_BY_BROADCAST",
                                "CHAT_FILTER_BY_UNREAD",
                                "CHAT_FILTER_BY_FAVORITED",
                                "CHAT_DELEGATE",
                                "CHAT_CHANGE_NAME",
                                "NOTES_VIEW",
                                "NOTES_ADD",
                                "CHAT_SEE_ALL",
                                "CHAT_VIEW_NUMBER",
                                "CHAT_MARK_UNREAD",
                                "CHAT_MARK_READ",
                                "CHAT_RELOAD_CHATS",
                                "CHAT_ADD_CHAT",
                                "CHAT_DELEGATION_LOGS",
                                "CHAT_VIEW_GROUP_CHATS",
                                "CUSTOM_FIELD_VIEW"}
        # -----------------------------------------
        # permissions adm -----------------

        json = {
            "auto_display_name_text": str(linha[0]),
            "auto_display_name": "on",
            "type": str(linha[2]),
            "permissions": permissions_analistas
        }

        response = session.post(url=url,data=json)

        if response.status_code == 200:
            print(f"Usuario atualizado : {linha[0]}")
        else:
            print(f"ERROR usuario : {linha[0]}")

if __name__ == '__main__':

    criar_user_chatguru()
    # update_user("C:/tester/update_teste.xlsx")