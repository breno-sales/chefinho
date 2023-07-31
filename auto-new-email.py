import pandas as pd

# tester1@stellaenergia.com.br,teste,tester,tester - Stella Energia,null,null,null,null,null,null,tester1@stellaenergia.com.br,null,null,null,null,null
# {email},{primeiro_nome},{ultimo_nome},{nome_exibicao},null,null,null,null,null,null,{email},null,null,null,null,null
# Nome de usuário,Nome,Sobrenome,Nome de exibição,Cargo,Departamento,Número comercial,Telefone comercial,Celular,Fax,Endereço de email alternativo,Endereço,Cidade,Estado ou província,CEP,País ou região



def teste():

    dados = pd.read_excel("C:/tester/tester.xlsx")

    linhas = []

    for i in range(0,len(dados['email'])):

        email = dados['email'][i]

        nome_usuario = dados['name'][i].lower()
        nome_usuario = nome_usuario.replace(" ", ".")

        primeiro_nome = nome_usuario[0:nome_usuario.find(".")]
        ultimo_nome = nome_usuario[nome_usuario.find(".")+1:]

        nome_exibicao = f'{dados["name"][i]} - Stella Energia'

        linha = f"{email},{primeiro_nome},{ultimo_nome},{nome_exibicao},null,null,null,null,null,null,{email},null,null,null,null,null"

        linhas.append(linha)

    carregar_dados = {"Nome de usuário,Nome,Sobrenome,Nome de exibição,Cargo,Departamento,Número comercial,Telefone comercial,Celular,Fax,Endereço de email alternativo,Endereço,Cidade,Estado ou província,CEP,País ou região":linhas}

    csv = pd.DataFrame(carregar_dados)
    print(csv)
    csv.to_csv("C:/tester/carregar.csv", index=False ,encoding='utf-8-sig')



if __name__ == '__main__':
    teste()