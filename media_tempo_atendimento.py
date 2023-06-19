import pandas as pd
from datetime import datetime
from dateutil.relativedelta import relativedelta
from openpyxl import *


def dados_excel():

    dados = pd.read_excel("C:/tester/dif_tempo.xlsx")
    print(dados)
    print(dados["Coluna1"][0])

    usuarios_json = []

    for i in range(1,len(dados["Coluna1"])):
        linha = []

        linha.append(dados["Coluna1"][i])
        linha.append(dados["Coluna2"][i])
        linha.append(dados["Coluna3"][i])
        linha.append(dados["Coluna4"][i])
        linha.append(dados["Coluna5"][i])
        linha.append(dados["Coluna6"][i])

        usuarios_json.append(linha)

    print(usuarios_json)

    return usuarios_json

def diferenca_tempo():

    dados = dados_excel()
    x = 1
    print(dados)
    for linha in dados:
        a = str(linha[4])
        b = str(linha[5])

        f = "%Y-%m-%d %H:%M"

        ini = datetime.strptime(a, f)
        fim = datetime.strptime(b, f)

        di = abs(relativedelta(ini, fim))



        if int(di.years) > 0:
            print(f'{di.years} anos, {di.months} meses, {di.days} dias, {di.hours}:{di.minutes}h')
        else:
            print(f'{di.months} meses, {di.days} dias, {di.hours}:{di.minutes}h')




if __name__ == "__main__":
    # dados_excel()
    diferenca_tempo()
