from jogo_RPG import *
from jogo_NUMS import *
from jogo_EVENTS import *

# ARTIGO

open_new_tab("webs\i1_intro.html")
while True:
    menuJogo()
    esp()
    opc = LeiaInt(3)
    SleepSys(1, 1)

    if opc == 1:
        final = RPG()

        if final == True:        # Final vivo com ou sem traje sem esperar ou esperando uma vez
            Vitoria()
        elif final == False:     # Final morto por dano
            Derrota()
        else:
            Especial()           # Final morto sem traje por esperar mais de uma vez
    
    elif opc == 2:
        Creditos()

    elif opc == 3:
        x = Sair()

        if x == True:
            break
        else:
            pass
