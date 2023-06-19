import requests
import re

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



def teste():

    session = get_cookies()
    url = "https://app4.zap.guru/chat/custom_fields/6357cf00640029c4f1392d63/view"

    response = session.post(url=url)
    resposta = response.text
    print(type(resposta))
    # # resposta = resposta.replace("",">"
    # #                                 "<")
    # resposta = resposta.replace(""
    #                             "","")
    # resposta = resposta.replace(">"
    #                             ""
    #                             ""
    #         "<", "")
    # resposta = resposta.replace(">"
    #                             ""
    #                             ""
    #                             ""
    #                             "<", "")
    resposta = resposta.replace("\n","")
    resposta = resposta.replace("\n\n", "")
    resposta = resposta.replace("\n\n\n", "")
    resposta = resposta.replace("\n\n\n\n", "")
    resposta = resposta.replace("\n\n\n\n\n", "")
    resposta = resposta.replace("\n\n\n\n\n\n", "")
    resposta = resposta.replace("\n\n\n\n\n\n\n", "")
    resposta = resposta.replace(" ","")
    print(resposta)
    print(type(resposta))
    return resposta

if __name__ == '__main__':

    tester = teste()
    print(type(tester))

    texto_a_ser_buscado_inicio = "Data_cancelamento:</td><tdclass=\"align-middleborder-top-0\"><textareadata-cf-id=\"646cba30f9b19b77896dfb53\"data-chat-id=\"6357cf00640029c4f1392d63\"class=\"custom_field_inputform-controlform-control-sm\">" #"<textareadata-cf-id=\"646cba30f9b19b77896dfb53\"data-chat-id=\"6357cf00640029c4f1392d63\"class=\"custom_field_inputform-controlform-control-sm\">"
    texto_a_ser_buscado_final = "</textarea></td></tr></table><hr><ahref=\"6357cf00640029c4f1392d63\"data-chat-id=\"6357cf00640029c4f1392d63\"class=\"custom-fields-modal-openbtnbtn-smbtn-outline-secondary\"><iclass=\"fafa-address-book\"></i>GerenciarCamposPersonalizados</a>"
    tamanho_texto_all = len(tester)
    tamanho_texto_buscado_inicio = len(texto_a_ser_buscado_inicio)
    tamanho_texto_buscado_final = len(texto_a_ser_buscado_final)

    posicao_texto_buscado_inicio = tester.find(texto_a_ser_buscado_inicio)
    posicao_texto_buscado_final = tester.find(texto_a_ser_buscado_final)
    print(tamanho_texto_all)
    print(tamanho_texto_buscado_inicio)
    print(tamanho_texto_buscado_final)
    print(posicao_texto_buscado_inicio)

    print(tester[posicao_texto_buscado_inicio + tamanho_texto_buscado_inicio:posicao_texto_buscado_final])
    print(tester)

