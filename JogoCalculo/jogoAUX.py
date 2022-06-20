from math import inf
from os import system
from time import sleep


def intro(titulo='n', *msg):
    if titulo != 'n':
        lin = '-' * (5 + len(titulo))
        print(f'{lin:^120}')
        print(f"{titulo:^120}")
        print(f'{lin:^120}')
    lista = msg
    for x in lista:
        centra(x)


def esp(x=0):
    print('\n' * (x-1))


def centra(msg, tam=120):
    print(f"{msg.center(tam)}") 


def menu(queb=0, queb2=0, queb3=0, titulo='n', subt='n', titf='n', *opcoes):
    lista = opcoes
    num = len(lista)
    if titulo != 'n':
        intro(titulo)
    if subt != 'n':
        centra(subt)
    for x in range(0, num):
        if queb != 0 or queb2 != 0 or queb3 != 0:
            if x + 1 < 10:
                print(f"""{f"[ 0{x+1} ] {lista[x]} {' ' * (45 - (len(lista[x]))) }":>90}""")
                if queb == x + 1 or queb2 == x + 1 or queb3 == x + 1:
                    print()
            if x + 1 >= 10:
                print(f"""{f"[ {x+1} ] {lista[x]} {' ' * (45 - (len(lista[x])))}":>90}""")
                if queb == x + 1 or queb2 == x + 1 or queb3 == x + 1:
                    print()
        else:
            if x + 1 < 10:
                print(f"""{f"[ 0{x+1} ] {lista[x]} {' ' * (45 - (len(lista[x]))) }":>90}""")
            if x + 1 >= 10:
                print(f"""{f"[ {x+1} ] {lista[x]} {' ' * (45 - (len(lista[x])))}":>90}""")
    if titf != 'n':
        centra(titf)


def LeiaInt(maximo=inf, centro=True, minimo=1, msg='Sua opção >>> ', msg_erro='Digite um número!'):
    if centro is False:
        while True:
            try:
                x = int(input(msg))
            except:
                print(msg_erro, '\n')
            else:
                if x > maximo or x < minimo:
                    print('Fora do limite!\n')
                else:
                    return x
    else:
        while True:
            try:
                x = CentraInput(msg)
                x = int(x)
            except:
                centra(msg_erro)
                esp()
            else:
                if x > maximo or x < minimo:
                    centra('Fora do limite!')
                    esp()
                else:
                    return x


def SleepSys(tempo=0, apagar=0):
    if tempo != 0:
        sleep(tempo)
    if apagar != 0:
        system("cls")


def CentraInput(msg):
    msg = msg.center(120).rstrip()
    x = input(f'{msg} ')
    return x


def nomeX_centro(perg, perg_erro, upper=False):
    while True:
        nome = CentraInput(perg)
        nome = nome.strip()
        if nome.isnumeric():
            centra(perg_erro)
            esp()
        if nome == '':
            centra('Digite algo!')
            esp()
        if nome.isnumeric() is False and nome != '':
            break
    if upper is False:
        return nome.capitalize()
    if upper is True:
        return nome.upper()
    if upper == 'title':
        return nome.title()
        

def status(vida, roupa):
    x = '=' * 21
    y = '-' * 21
    centra(x)
    centra('Status')
    centra(x)
    centra(f'| {vida} corações |')
    centra(y)
    centra('Equipamento')
    centra(y)
    if roupa == True:
        centra(f'| Roupa de Proteção |')
    else:
        if vida >= 10:
            centra('|   Nenhum    |')
        else:
            centra('|   Nenhum   |')
    centra(x)


def passar():
    input('\nPressione ENTER para continuar...')


def Quest():
    while True:
        try:
            x = CentraInput('Resposta: ')
            x = int(x)
        except:
            centra('Digite um número!')
            esp()
        else:
            return x
