



def classificacao_muito_frio(temperatura: float):

    if temperatura <= 15:
        retorno = 100
    elif temperatura > 15 and temperatura <= 20:
        retorno = 100 - 20*(temperatura - 15)
    else:
        retorno = 0

    return retorno

def classificacao_frio(temperatura: float):

    if temperatura >= 15 and temperatura <= 20:
        retorno = 0 + 20*(temperatura - 15)
    elif temperatura >= 20 and temperatura <= 25:
        retorno = 100 - 20*(temperatura - 20)
    else:
        retorno = 0

    return retorno

def classificacao_moderado(temperatura: float):

    if temperatura >= 20 and temperatura <= 25:
        retorno = 0 + 20*(temperatura - 20)
    elif temperatura >= 25 and temperatura <= 30:
        retorno = 100 - 20*(temperatura - 25)
    else:
        retorno = 0

    return retorno

def classificacao_calor(temperatura: float):

    if temperatura >= 25 and temperatura <= 30:
        retorno = 0 + 20*(temperatura - 25)
    elif temperatura >= 30 and temperatura <= 35:
        retorno = 100 - 20*(temperatura - 30)
    else:
        retorno = 0

    return retorno

def classificacao_muito_calor(temperatura: float):

    if temperatura >= 35:
        retorno = 100
    elif temperatura >= 30 and temperatura <= 35:
        retorno = 0 + 20*(temperatura - 30)
    else:
        retorno = 0

    return retorno

def teste_de_temperatura(temperatura: float):

    muito_frio = classificacao_muito_frio(temperatura)
    frio = classificacao_frio(temperatura)
    moderado = classificacao_moderado(temperatura)
    calor = classificacao_calor(temperatura)
    muito_calor = classificacao_muito_calor(temperatura)

    if muito_frio > frio:
        print(f"Hoje o dia está {muito_frio:.2f}% classificado como MUITO FRIO")
    elif muito_frio == frio and muito_frio != 0:
        print(f"Hoje está uma sensação entre MUITO FRIO e FRIO")
    elif frio > moderado:
        print(f"Hoje o dia está {frio:.2f}% classificado como FRIO")
    elif frio == moderado and frio != 0:
        print(f"Hoje está uma sensação entre FRIO e MODERADO")
    elif moderado > calor:
        print(f"Hoje o dia está {moderado:.2f}% classificado como MODERADO")
    elif moderado == calor and moderado != 0:
        print(f"Hoje está uma sensação entre MODERADO e CALOR")
    elif calor > muito_calor:
        print(f"Hoje o dia está {calor:.2f}% classificado como CALOR")
    elif calor == muito_calor and calor != 0:
        print(f"Hoje está uma sensação entre CALOR e MUITO CALOR")
    else:
        print(f"Hoje o dia está {muito_calor:.2f}% classificado como MUITO CALOR")





if __name__ == "__main__":

    # temperatura = 30.15

    print(f"Bem vindo a classificação de sensação térmica, para classificarmos entre:\n\n"
          f"-Muito frio\n"
          f"- Frio\n"
          f"- Moderado\n"
          f"- Calor\n"
          f"- Muito Calor\n\n"
          f"Insira a temperatura que está marcando atualmente como no exemplo a seguir:\n"
          f"(ex: 28.3)\n")

    temperatura = float(input("temperatura atual = "))
    print("\n")
    print(f"temperatura atual = {temperatura}")

    teste_de_temperatura(temperatura)

    # teste de porcentagem de cada tipo --------------------------------------
    # print(classificacao_muito_frio(temperatura))
    # print(classificacao_frio(temperatura))
    # print(classificacao_moderado(temperatura))
    # print(classificacao_calor(temperatura))
    # print(classificacao_muito_calor(temperatura))
# picos -----------------
#
# muito frio  = 15
# frio = 20
# moderado = 25
# calor = 30
# muito calor  = 35