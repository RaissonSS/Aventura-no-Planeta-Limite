from jogoAUX import *
from webbrowser import open_new_tab

def menuJogo():
    menu(0, 0, 0, 'RPG Aventura no Planeta Limite', 'A deriva em meio a hostilidade', 'n', 'Iniciar História',
    'Créditos', 'Sair')


def Creditos():
    intro('Créditos', 'Esta aplicação Web com Python foi desenvolvida por:', 'Raisson Souza', '', 'Contato:',
    'Email: silveiraraisson@gmail.com', 'Youtube: RaissonSS edições')
    passar()
    SleepSys(1, 1)


def Sair():
    menu(0,0,0, 'Você tem certeza que deseja sair?', 'n', 'n', 'Sim', 'Não')
    x = LeiaInt(2)
    if x == 1:
        return True
    else:
        SleepSys(0, 1)
        return False
        
# ------------------------------------------- TODOS OS FINAIS ----------------------------------------------        


def Vitoria():
    open_new_tab('webs\c3_vitoria.html')
    SleepSys(0, 1)


def Derrota():
    open_new_tab('webs\c2_derrota.html')
    esp(2)
    centra('Resgatar pessoas perdidas em planetas hostis não é seu forte.')
    centra('Tente jogar novamente!')
    passar()
    SleepSys(1, 1)


def Morte(vida, roupa):
    open_new_tab('webs\c1_Qmorte.html')
    status(vida, roupa)
    esp()
    centra('Você está próximo da morte! Tenha muito cuidado!')
    passar()
    SleepSys(1, 1)


def Especial():
    open_new_tab('webs\c4_finalEspecial.html')
    esp(5)
    passar()
    SleepSys(1, 1)
