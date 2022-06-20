# SIMPLE SCRIPT PARA MELHORAMENTO DA INTERFACE DO PROGRAMA

def w(obj, espn=20):
    return f"{' ' * (espn-len(obj))}"


def intro(titulo='n', *msg):
    if titulo != 'n':
        lin = '-' * (5 + len(titulo))
        print(f'{lin:^120}')
        print(f"{titulo:^120}")
        print(f'{lin:^120}')
    lista = msg
    for x in lista:
        centra(x)


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


def creditos():
    intro('CRÉDITOS', 'Programa criado por RaissonSS.', 'Twitter: @RaissonSS', 'Email: silveiraraisson@gmail.com')


def esp(x=0):
    print('\n' * (x-1))


def desafio(titulo, sub, sub2='n', sub3='n', *opc):
    intro(titulo)
    centra(sub)
    if sub2 != 'n':
        centra(sub2)
    if sub3 != 'n':
        centra(sub3)
    esp()
    lista = opc
    tam = len(lista)
    for x in range(0, tam):
        if x + 1 < 10:
            print(f"""{f"[ 0{x+1} ] {lista[x]} {' ' * (30 - (len(lista[x]))) }":>77}""")
        if x + 1 >= 10:
            print(f"""{f"[ {x+1} ] {lista[x]} {' ' * (30 - (len(lista[x])))}":>77}""")


def RPG_PRINT(msg):
    print(' ' * 5, f'{msg}')


def RPG_TITLE(msg, info):
    print(f'| --- {msg} --- |'.center(100))
    print(f'| VIDA = {info[0]} | ATAQUE = {info[1]} | XP = {info[2]} |'.center(100))


def RPG_MENU(opc):
    num = len(opc)
    for x in range(0, num):
        if x + 1 < 10:
            RPG_PRINT(f'   [0{x + 1}] {opc[x]}')
        if x + 1 >= 10:
            RPG_PRINT(f'   [{x + 1}] {opc[x]}')


def RPG_OPC(lim):
    while True:
        try:
            x = int(input('Qual sua a sua escolha? '))
        except:
            RPG_PRINT('Escreva um número!')
            esp()
        else:
            if x > lim or x < 1:
                RPG_PRINT('Fora do limite!')
                esp()
            else:
                return x


def RPG(evento, info, status, *msg):
    RPG_TITLE(evento, info)
    esp()
    for x in msg:
        RPG_PRINT(x)
    if status != 'n':
        RPG_PRINT(f'>>> Seu status: {status}.')


def RPG_ACTION(name, explanation, *opc):
    esp()
    RPG_PRINT(f'{name}, o que voce vai fazer?')
    RPG_MENU(opc)
    esp()
    RPG_PRINT(explanation)
    esp()
    x = RPG_OPC(len(opc))
    esp()
    return x


def RPG_CONCLUSION(event, explanation, info, status, *msg):
    RPG_TITLE(event, info)
    esp()
    for x in msg:
        RPG_PRINT(x)
    if status != 'n':
        esp()
        RPG_PRINT(f'Seu status >>> {status}')
    if explanation != 'n':
        esp()
        RPG_PRINT(explanation)


def enumeration(lista, divisions, tam1=20, tam2=20, tam3=20):
    asp = " " * 35
    if divisions == 1:
        for x, y in enumerate(lista):
            if x + 1 < 10:
                print(f'{asp}|0{x + 1}| {y}')
            else:
                print(f'{asp}|{x + 1}| {y}')
    if divisions == 2:
        for x, y in enumerate(lista):
            if x + 1 < 10:
                print(f'{asp}|0{x + 1}| {y[0]} {w(y[0], tam1)} {y[1]}')
            else:
                print(f'{asp}|{x + 1}| {y[0]} {w(y[0], tam1)} {y[1]}')
    if divisions == 3:
        for x, y in enumerate(lista):
            if x + 1 < 10:
                print(f'{asp}|0{x + 1}| {y[0]} {w(y[0], tam1)} {y[1]} {w(y[1], tam2)} {y[2]}')
            else:
                print(f'{asp}|{x + 1}| {y[0]} {w(y[0], tam1)} {y[1]} {w(y[1], tam2)} {y[2]}')
    if divisions == 4:
        for x, y in enumerate(lista):
            if x + 1 < 10:
                print(f'{asp}|0{x + 1}| {y[0]} {w(y[0], tam1)} {y[1]} {w(y[1], tam2)} {y[2]} {w(y[2], tam3)} {y[3]}')
            else:
                print(f'{asp}|{x + 1}| {y[0]} {w(y[0], tam1)} {y[1]} {w(y[1], tam2)} {y[2]} {w(y[2], tam3)} {y[3]}')
