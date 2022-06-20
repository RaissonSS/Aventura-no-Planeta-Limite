from jogoAUX import *
from webbrowser import open_new_tab
from jogo_NUMS import *
from jogo_EVENTS import Morte

def morte():
    pass

def RPG():

    # -------------------------------------------------------- INTRODUÇÃO ----------------------------------

    espaco = '=' * 40
    centra(espaco)
    centra("Seu personagem precisa de um nome!")
    nome = nomeX_centro('Qual o seu nome? ', 'Digite um nome válido!')
    esp()
    SleepSys(1)
    centra(f'Prazer em te conhecer {nome}! Tenha uma ótima aventura!')
    SleepSys(4, 1)
    esp(2)
    intro('Iniciando contagem regressiva...')
    SleepSys(3, 1)
    num3()
    SleepSys(2, 1)
    num2()
    SleepSys(2, 1)
    num1()
    SleepSys(2, 1)

    open_new_tab("webs\i2_viagem.html")
    input('\n\n\n\n\nPressione ENTER para continuar...')
    SleepSys(0.5, 1)

    open_new_tab("webs\i3_intro2.html")
    input('\n\n\n\n\nPressione ENTER para continuar...')
    SleepSys(0.5, 1)

    open_new_tab("webs\i4_atmosfera.html")
    input('\n\n\n\n\nPressione ENTER para continuar...')
    SleepSys(0.5, 1)

    open_new_tab("webs\i5_coordenada.html")
    input('\n\n\n\n\nPressione ENTER para continuar...')
    SleepSys(0.5, 1)

    open_new_tab("webs\i6_comp.html")
    input('\n\n\n\n\nPressione ENTER para continuar...')
    SleepSys(0.5, 1)

    esp(2)
    centra('Você está prestes a aterrisar no planeta, mas pilotar não é seu forte e')
    centra('ninguém o avisou que os ventos da atmosfera estão muito fortes...')
    esp()
    centra('Sua nave é arrastada pelas densas e traiçoeiras nuvens de Limite!')

    input('\nAperte ENTER para Continuar...')
    SleepSys(1, 1)
    open_new_tab("webs\i6-2_queda.html")

    vida = 20
    roupa = False
        
    esp(2)
    status(vida, roupa)
    esp()
    centra('Esse é seu status atual.')
    centra('A partir de agora, você precisa responder algumas questões')
    centra('matemáticas fornecidas pelo seu computador para a reprogramação do mesmo.')
    esp()
    centra('A cada questão errada, você sofrerá 3 corações de dano!')
    input('\nPressione ENTER para continuar...')
    SleepSys(1, 1)

    acertos = 0

    # --------------------------------------- QUESTÃO 1 ---------------------------------------------------

    open_new_tab('webs\i7_q1.html')
    esp(2)
    centra('Digite a resposta:')
    esp()
    resp = Quest()
    if resp == 27:
        acertos += 1
        roupa = True
    else:
        vida -= 3
        vida -= 1
    SleepSys(1, 1)

    esp(2)
    if roupa == True:
        centra('Enquanto você pensava na resposta, achou seu traje de proteção!')
        centra('agora você está protegido da atmosfera tóxica e não sofrerá danos colaterais em eventos aleatórios!')

    else:
        centra('Enquanto você pensava na resposta, achou seu traje de proteção!')
        centra('Mas ele está completamente inutilizado...')
        esp()
        centra('Você sofrerá +1 de dano por questão errada e danos colaterais em eventos aleatórios.')
    esp()
    status(vida, roupa)
    passar()
    SleepSys(1, 1)


    # --------------------------------------- EVENTO 1 ---------------------------------------------------

    esp(2)
    centra('Se afastando de sua nave, você se depara com uma floresta colorida e de aparência "mágica".')
    centra('Uma árvore em específico tem frutos brilhantes que de dão água na boca e afloram sua fome,')
    centra('seria uma boa idéia comer alguns?')
    esp()
    menu(0, 0, 0, 'EVENTO 01', 'Você come os frutos dessa árvore?', 'n', 'Sim', 'Não')
    resp = LeiaInt(2)
    esp()

    especial1 = False

    if resp == 1:
        centra('Experimentar aqueles frutos brilhantes não foi uma má ideia, você não está mais com fome.')
        especial1 = True
    else:
        centra('É melhor evitar algum envenenamento mesmo, você continua seu caminho com fome.')
    if roupa == False:
        centra('Você sente uma certa ardência no rosto, é uma lástima que seu traje tenha sido destruído,')
        centra('pois se tivesse ele, suportaria os gases tóxicos da atmosfera!')
        vida -= 2
        esp()
        centra('-2 de vida.')
    passar()
    SleepSys(1, 1)
    

    # --------------------------------------- QUESTÃO 2 ---------------------------------------------------

    open_new_tab('webs\i8_q2.html')
    esp(2)
    centra('Digite a resposta:')
    esp()
    resp = Quest()
    if resp == 96:
        acertos += 1
    else:
        vida -= 3
    if roupa == False:
        vida -= 1
    SleepSys(1, 1)

    status(vida, roupa)
    passar()
    SleepSys(1, 1)

    # VIDA 10

    # --------------------------------------- EVENTO 2 ---------------------------------------------------

    esp(2)
    centra('Há uma divisão no caminho!')
    esp()
    centra('Logo em frente, na sua direita há um campo de geiseres que soltam um gás úmido e amarelado.')
    centra('Na sua esquerda há um campo cheio de pequenas rochas lascadas e pontiagudas.')
    centra('Entre esses campos há um pequeno corrego de água roxa que borbulha de pequenos peixes.')
    esp()
    menu(0,0,0, 'EVENTO 02', 'Qual caminho você escolhe?', 'n', 'Campo de Geiseres', 'Campo de rochas lascadas',
    'Corrego de água roxa', 'Circular a região e seguir em frente (evitando tudo)')
    resp = LeiaInt(4)
    esp(2)

    if resp == 1:
        centra('Caminhar em meio aos furiosos geiseres esquenta seu corpo, mas você os deixa pra trás.')
        if roupa == False:
            centra('Só não ficará para trás suas narinas, olhos e ouvidos ardidos pelo gás tóxico.')
            centra('-3 de vida')
            vida -= 3
    elif resp == 2:
        centra('Caminhar em meio às rochas pontiagudas não é fácil, algumas atravessam suas botas e fincam seus pés!')
        if roupa == True:
            centra('Devido a seu traje de proteção, as rochas só aparentaram fincá-lo na verdade.')
        else:
            centra('É bom arrumar alguns curativos, e rápido!')
            centra('-3 de vida')
            vida -= 3
    elif resp == 3:
        centra('Andar com uma água quente e roxa até a cintura com criaturas te pinicando nas pernas não é confortável.')
        if roupa == True:
            centra('Devido a seu traje de proteção, nenhuma criatura lhe morde e nem a água toca em sua pele.')
        else:
            centra('Um bicho escuro e com uma cauda longa lhe desfere um golpe nas coxas, é bom achar uma pomada...')
            centra('-3 de vida')
            vida -= 3
    else:
        centra('Evitar toda a região por medo de consequências lhe custa muito tempo, a lua vermelha atéatravessou o céu 2 vezes.')
        esp()
        if roupa == False:
            centra('Gastar tanto tempo precioso em um planeta com atmofera tóxica e sem um traje foi uma péssima idéia...')
            centra('-3 de vida')
            vida -= 3
    passar()
    SleepSys(1, 1)

    # VIDA 7

    # --------------------------------------- ALERTA MORTE ---------------------------------------------------

    if vida <= 10:
        Morte(vida, roupa)
    
    # --------------------------------------- QUESTÃO 03 ------------------------------------------------------

    open_new_tab('webs\i9_q3.html')
    esp(2)
    centra('Digite a resposta:')
    esp()
    resp = Quest()
    if resp == -1:
        acertos += 1
    else:
        vida -= 3
    if roupa == False:
        vida -= 1
    SleepSys(1, 1)

    status(vida, roupa)
    passar()
    SleepSys(1, 1)

    # VIDA 3

    # --------------------------------------- ALERTA MORTE ---------------------------------------------------

    if vida <= 10:
        Morte(vida, roupa)

    # --------------------------------------- QUESTÃO 04 ------------------------------------------------------

    open_new_tab('webs\i10_q4.html')
    esp(2)
    centra('Digite a resposta:')
    esp()
    resp = Quest()
    if resp == 30:
        acertos += 1
    else:
        vida -= 3
    if roupa == False:
        vida -= 1
    SleepSys(1, 1)

    # VIDA -1

    # --------------------------------------- ALERTA MORTE ---------------------------------------------------

    if vida <= 0:
        return False

    if vida <= 10:
        Morte(vida, roupa)
    else:
        status(vida, roupa)
        passar()
        SleepSys(1, 1)

    # --------------------------------------- EVENTO 03 ---------------------------------------------------

    esp(2)
    centra('Uma luz forte e uma coluna de fumaça ao longe!')
    esp()
    centra('A noite se aproxima e com ela o terrível frio, você deve tomar uma decisão.')
    centra('Aquela grande chama de luz com uma coluna de fumaça significa calor ou a nave caída do cientista!')
    centra('Daria para ver melhor se tudo aquilo não estivesse atrás de um grande morro...')
    esp()
    menu(0,0,0, 'EVENTO 03', 'Faça sua escolha', 'n', 'Continuar trajeto', 'Procurar local seguro para dormir')
    resp = LeiaInt(2)
    esp()

    especial2 = False

    if resp == 1:
        centra('Você decide continuar seu trajeto em meio ao dia se encerrando, as trevas começam a engoli-lo...')
        centra('O frio toma conta de seu corpo no meio do trajeto...')
        centra('As lindas auroras boreais no céu e os insetos místicos de Limite se mostram para você...')
        esp()
        if roupa == True:
            centra('Seu traje de proteção te impede de ter uma hipotermia.')
        else:
            centra('Você contrai uma hipotermia devido ao frio intenso.')
            centra('-3 de vida')
            vida -= 3
            if vida <= 0:
                passar()
                SleepSys(1, 1)
                esp(2)
                centra('Você estava subindo o morro tremendo de frio, até que avista a nave do cientista pegando fogo.')
                centra('O mesmo construia um módulo de fuga próximo dela, mas você está fraco demais para gritar por ajuda.')
                esp()
                centra('Você morre.')
                passar()
                SleepSys(1, 1)
                return False
        passar()
        SleepSys(1, 1)

        esp(2)
        centra('Você termina de subir o morro e avista o cientista construindo um módulo')
        centra('de fuga próximo de sua nave que pegava fogo.')
        esp()
        centra('Você corre até ele e passa o resto da noite em segurança, aquecido e alimentado devido a seus mantimentos.')
        esp()

    elif resp == 2:
        especial2 = True
        centra('Você decide procurar um local para dormir.')
        passar()
        SleepSys(1, 1)
        esp()
        menu(0, 0, 0, 'Onde você irá dormir?', 'n', 'n', 'Dentro de um tronco aberto caído', 'Uma caverna', 'Próximo do córrego de água roxa')
        x = LeiaInt(3)
        esp()
        if x == 1:
            centra('Você passa a noite bem devido as propriedades térmicas da madeira.')
            centra('A madeira também impede que você seja exposto diretamente ao ar tóxico da atmosfera')
            centra('filtrando suas toxinas')
            esp()
            centra('+ 3 de vida')
            esp()
            vida += 3
        elif x == 2:
            centra('Você passa a noite com frio dentro daquela caverna.')
            centra('-3 de vida')
            esp()
            vida -= 3
            if vida <= 0:
                centra('Mas infelizmente o frio foi intenso demais para sua saúde já prejudicada...')
                centra('Você morre.')
                passar()
                SleepSys(1, 1)
                return False
        elif x == 3:
            centra('Você passa a noite deitado próximo do córrego de água roxa que emana um calor natural.')
            centra('Porém... O vapor da água também é tóxico assim como sua atmosfera...')
            esp()
            centra('-3 de vida')
            esp()
            vida -= 3
            if vida <= 0:
                centra('Você morre em paz e aquecido...')
                passar()
                SleepSys(1, 1)
                return False

    # VIDA -4
    

    # --------------------------------------- QUESTÃO 05 ---------------------------------------------------

    centra('No meio da noite você têm um sonho...')
    passar()
    SleepSys(1, 1)

    open_new_tab('webs\i11_q5.html')
    esp(2)
    menu(0,0,0, 'Qual sua resposta?', 'n', 'n', '1 sobre 2 raiz de 3', '1 sobre 3', 'raiz de 3 sobre raiz de 3', 'raiz de 3 sobre 6')
    esp()
    resp = LeiaInt(4)
    esp()

    if resp == 4:
        acertos += 1
    
    centra('Você acorda assustado com um sonho tão realista, mas nada aconteceu com você.')
    passar()
    SleepSys(1, 1)

    if especial2 == True:
        esp(2)
        centra('Voçê acorda bem e descançado, preparado para seguir caminho e chegar até o cientista.')
        esp()
        centra('Subindo o morro, você vê a nave dele incendiada e quase que completamente destruída')
        centra('e o mesmo, construía um pequeno módulo de fuga com peças que restaram de sua nave.')
        passar()
        SleepSys(1, 1)

    # --------------------------------------- QUESTÃO 06 ---------------------------------------------------

    esp()
    centra('RETA-FINAL')
    esp()
    centra('No horário em que as duas estrelas estavam no topo do céu, vocês julgam ser horário de almoço.')
    centra('O almoço são algumas frutas brilhantes de uma floresta próxima na qual o cientista colheu.')
    esp()

    if especial1 == True:
        centra('Você comenta com o cientista de que havia comido as mesmas anteriormente e então comem elas juntos.')
    else:
        centra('Você tem um certo receio de comer elas... Mas não iria questionar um cientista renomado...')

    passar()
    SleepSys(1, 1)

    esp(2)
    centra('Seu computador quântico apita novamente e manda você realizar outra questão matemática,')
    centra('que bom que tem um cientista ao seu lado...')

    open_new_tab('webs\i12_q6.html')
    esp(2)
    centra('Digite a resposta:')
    esp()
    resp = Quest()
    if resp == 4:
        acertos += 1
    else:
        vida -= 3
    if roupa == False:
        vida -= 1
    SleepSys(1, 1)


    # VIDA -8

    # --------------------------------------- ALERTA MORTE ---------------------------------------------------

    if vida <= 0:
        return False

    if vida <= 10:
        Morte(vida, roupa)
    else:
        status(vida, roupa)
        passar()
        SleepSys(1, 1)

    # --------------------------------------- DESFECHO ---------------------------------------------------

    esp()
    centra('Após realizarem a última questão, o computador se reinicia e sua pontuação começa a ser calculada...')
    esp()
    centra('A situação teria menos tensão se o cientista não o olhasse torto após se dar conta que você')
    centra('resolveu todas as outras anteriores sem ele, ainda mais quando você quase deu uma resposta errada na')
    centra('questão anterior...')
    passar()
    SleepSys(1, 1)
    esp()
    centra(f'O computador fez seu calculo, você acertou {acertos} questões.')
    tempo = (6 - acertos) * 3
    esp()
    

    if tempo == 0:
        centra('Parabéns! Você acertou todas as questões!')
        centra('O computador é reprogramado imediatamente e recupera seu poder imensurável de processamento.')
        esp()
        centra('Você utiliza seu computador para instalar todos os softwares necessários e atualizados na nave improvisada')
        centra('e embarca nela junto com o cientista.')
        esp()
        centra(f'{nome}, você venceu!')
        passar()
        SleepSys(0, 1)
        return True

    else:
        centra(f'Você acertou {acertos} questões, o que significa que seu computador levará {tempo} dias para ser restaurado.')
        centra(f'Tempo para a restauração: {6 - acertos} (Respostas erradas) x 3 = {tempo} (Dias de espera)')
        esp()

        if roupa == False and tempo == 3:
            centra('Por sua sorte, mesmo sem um traje de proteção, o cientista, que possui um,')
            centra('Cuida de você com seu conhecimento medicinal e o impede de morrer devido à toxidade de Limite.')
            esp()
            centra('Quando o computador completou seu tempo de restauração, você e o cientista decolam juntos')
            centra('e finalmente escapam de Limite.')
            esp()
            centra(f'{nome}, você venceu!')
            passar()
            SleepSys(0, 1)
            return True

        elif roupa == False:
            centra('Infelizmente, o cientista, que está de traje, não tem outro traje de proteção para você...')
            centra('E mesmo sob cuidados médicos, ficar mais tempo nesse planeta tóxico irá matá-lo...')
            passar()
            SleepSys(1, 1)
            esp(2)
            centra('Você infelizmente morre no dia seguinte devido a múltipla falência de órgãos causada pelo ar tóxico de Limite.')
            esp()
            centra('Porém, o cientista escapa e leva seu corpo junto.')
            centra('Graças a você e seu computador quântico, o cientista foi capaz de escapar de Limite')
            centra('e levar informações cruciais sobre o planeta para a humanidade.')
            passar()
            SleepSys(1, 1)
            return 'FinalEspecial'
        
        else:
            centra('Graças aos trajes de proteção, você e o cientista são capazes de suportar a toxidade do planeta')
            centra(f'e fugir depois de {tempo} dias!')
            esp()
            centra('Você utiliza seu computador para instalar todos os softwares necessários e atualizados na nave improvisada')
            centra('e embarca nela junto com o cientista.')
            esp()
            centra('Vocês decolam...')
            return True
