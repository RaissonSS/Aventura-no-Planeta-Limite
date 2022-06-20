# SIMPLE SCRIPTS PARA ANÁLISE DE DADOS

from datetime import date, datetime
from math import sqrt, inf
from time import sleep
from os import system
from outros.SS_INTERFACE import esp, centra


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


def LeiaFloat(maximo=inf, centro=True, minimo=0, msg='Sua opção >>> ', msg_erro='Digite um número!'):
    if centro is False:
        while True:
            try:
                x = float(input(msg))
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
                x = float(x)
            except:
                print(msg_erro, '\n')
                centra(msg_erro)
                esp()
            else:
                if x > maximo or x < minimo:
                    print('Fora do limite!\n')
                else:
                    return x


def w(obj, espn=20):
    return f"{' ' * (espn-len(obj))}"
# usa-se como referencia o objeto anterior para a medição de espaço, não o seguinte!


def Cubert(x):
    if x < 0:
        x = abs(x)
        cube_root = x ** (1 / 3) * (-1)
    else:
        cube_root = x ** (1 / 3)
    return cube_root


def Raiz(fora, dentro):
    total = fora * (sqrt(dentro))
    return total


def SleepSys(tempo=0, apagar=0):
    if tempo != 0:
        sleep(tempo)
    if apagar != 0:
        system("cls")


def CentraInput(msg):
    msg = msg.center(120).rstrip()
    x = input(f'{msg} ')
    return x


def nomeX(perg, perg_erro, upper=False):
    while True:
        nome = str(input(perg))
        nome = nome.strip()
        if nome.isnumeric():
            print(f'{perg_erro}\n')
        if nome == '':
            print('Digite algo!\n')
        if nome.isnumeric() is False and nome != '':
            break
    if upper is False:
        return nome.capitalize()
    if upper is True:
        return nome.upper()
    if upper == 'title':
        return nome.title()


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


def dataX_centro(now, msg='Informe a data: [ dia/mes ] '):
    if now is True:
        if date.today().day < 10 and date.today().month > 10:
            return f'0{date.today().day}/{date.today().month}/{date.today().year}'
        if date.today().month < 10 and date.today().day > 10:
            return f'{date.today().day}/0{date.today().month}/{date.today().year}'
        if date.today().day < 10 and date.today().month < 10:
            return f'0{date.today().day}/0{date.today().month}/{date.today().year}'
        else:
            return f'{date.today().day}/{date.today().month}/{date.today().year}'
    else:
        ano = date.today().year
        while True:
            data = CentraInput(f'{msg}')
            try:
                data1 = int(data[0:2])
                data2 = int(data[3:5])
            except:
                esp()
                centra('Voce digitou a data de forma incorreta, tente novamente!')
                esp()
            else:
                if len(data) > 5 or len(data) < 5 or data == '':
                    esp()
                    centra('Voce digitou a data de forma incorreta, tente novamente!')
                elif data1 > 31 or data1 <= 0 or data2 > 12 or data2 <= 0:
                    esp()
                    centra('Sua data está errada, tente novamente!')
                else:
                    data1 = int(data[0:2])
                    data2 = int(data[3:5])
                    if data2 < 10:
                        data2 = f'0{data2}'
                    if data1 < 10:
                        data1 = f'0{data1}'
                    return f'{data1}/{data2}/{ano}'
                esp()


def dataX(now, msg='Informe a data: [ dia/mes ] '):
    if now is True:
        return f'{date.today().day}/{date.today().month}/{date.today().year}'
    else:
        ano = date.today().year
        while True:
            data = str(input(f'\n{msg}'))
            try:
                data1 = int(data[0:2])
                data2 = int(data[3:5])
            except:
                print('\nVoce digitou a data de forma incorreta, tente novamente!')
            else:
                if len(data) > 5 or len(data) < 5 or data == '':
                    print('\nVoce digitou a data de forma incorreta, tente novamente!')
                elif data1 > 31 or data1 <= 0 or data2 > 12 or data2 <= 0:
                    print('\nVoce digitou a data de forma incorreta, tente novamente!')
                else:
                    data1 = int(data[0:2])
                    data2 = int(data[3:5])
                    if data2 < 10:
                        data2 = f'0{data2}'
                    if data1 < 10:
                        data1 = f'0{data1}'
                    return f'{data1}/{data2}/{ano}'
                esp()


def horaX(now, msg='Informe a hora: ', msg_erro='Formato de horário incorreto!'):
    if now is True:
        x = f'{datetime.now()}'
        return x[11:16]
    else:
        print('Digite o horário neste formato:')
        print('Ex: 12:30 | 08:15 | 21:20')
        esp()
        while True:
            hora = input(msg)
            if hora[0:2].isnumeric() and len(hora[0:2]) == 2 and len(hora[3:6]) == 2 and hora[3:6].isnumeric():
                hour = int(hora[0:2])
                mins = int(hora[3:6])
                if hour > 23 or hour < 0 or mins > 59 or mins < 0:
                    print('Horário inválido!')
                else:
                    return f'{hora[0:2]}:{hora[3:6]}'
            else:
                centra(msg_erro)
            esp()


def horaX_centro(now, msg='Informe a hora: ', msg_erro='Formato de horário incorreto!'):
    if now is True:
        x = f'{datetime.now()}'
        return x[11:16]
    else:
        centra('Digite o horário neste formato:')
        centra('Ex: 12:30 | 08:15 | 21:20')
        esp()
        while True:
            hora = CentraInput(msg)
            if hora[0:2].isnumeric() and len(hora[0:2]) == 2 and len(hora[3:6]) == 2 and hora[3:6].isnumeric():
                hour = int(hora[0:2])
                mins = int(hora[3:6])
                if hour > 23 or hour < 0 or mins > 59 or mins < 0:
                    centra('Horário inválido!')
                else:
                    return f'{hora[0:2]}:{hora[3:6]}'
            else:
                centra(msg_erro)
            esp()
