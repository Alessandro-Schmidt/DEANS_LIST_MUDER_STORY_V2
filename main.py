# Neste código existem bibliotecas que precisam ser instaladas no python. São elas a pyfiglet e a tabulate. Sugerimos baixar na máquina com os comandos pip ou rodar este código no Replit. 

import pyfiglet
from tabulate import tabulate
import time
titulo = pyfiglet.figlet_format('DEANS LIST', font='banner3-D')
sub_title = pyfiglet.figlet_format('Um misterio de ASSASSINATO', font='standard')
print(titulo)

print(sub_title)

# início da história
print('--- Contexto ---\nNo auge da Guerra Fria, uma semana após a crise dos mísseis de Cuba e início do bloqueio continental, a América Latina vive um momento de tensão sem igual.\n\nNa PUCPR não é diferente.\n\nEspiões andam disfarçados entres os alunos, com o objetivo de roubar os postits dos requisitos do projeto da Bomba de Hidrogênio.\n\nO prédio da Escola Politécnica é o mais vigiado do Paraná. Não é permitida a entrada de pessoas não autorizadas nas aulas de BES.\n\nO assassinato da reitora veio como um choque para os estudantes, e está sendo abafado pela mídia e pela Universidade.\n\nVocê foi designado pelo Governo Federal para solucionar o mistério. A justiça está nas suas mãos. Descubra o autor do crime, o local do crime e a arma do crime. SEJA RÁPIDO! O responsável pode estar fugindo.\n\n')
print('-'*len('Vítima: Andreia Malucelli, decâna da Escola Politécnica'))
print('RELATÓRIO DA INVESTIGAÇÃO\nData do crime: 20/10/1962\nVítima: Andreia Malucelli, decâna da Escola Politécnica.\nLocal: Sigiloso.\nArma: Sigiloso.\nAutor do crime: em investigação.')
print('-'*len('Vítima: Andreia Malucelli, decâna da Escola Politécnica'))
print('\n\n-- HIPÓTESES --\n\n')
print('LOCAL -- \n\na) O assassinato foi feito ao ar livre.\n\nb) Foram encontrados documentos queimados da decana no lixo antes da saída da PUCPR.\n\nc) Ela foi vista correndo em diração à Escola Politécnica, com uma bolsa preta...\n\nd) Uma bolsa de cor desbotada foi achada nas margens do rio que passa pela PUCPR.\n\n')
print('ARMA --\n\na) Uma fita cassete pequena foi encontrada junto aos documentos no lixo. Nesta fita, haviam instruções de como fugir do país.\n\nb) O General da CIA dentro da PUCPR possui uma arma no seu escritório\n\nc) Espiões da KGB usam armas pouco convencionais para evitar suspeitas.\n\nd) Um compasso sujo foi encontrado junto com a identidade de um duplo espião.\n\ne) Um notebook completamente formatado foi derrubado próximo a cena do crime.\n\n')
print('SUSPEITO --\n\na) Se sabe da existência de no mínimo uma espiã da KGB na Universidade.\n\nb) Não era do interesse americano, a morte da decana.\n\nc) O assassino não era neutro.\n\nd) É conhecido o envolvimento de pelo menos um dos monitores com a KGB.\n\ne) Existem ao menos, dois espiões duplos na Universidade.\n\nf) Se sabe que Alessandro já estava desconfiado de algo...')
print('\n\nFATOS IMPORTANTES\n\nf) Um dos agentes duplos não tem relação alguma com BES.\n\ng) Você investigar alguém pode causar a sua morte.\n\nh) Cuidado com pistas falsas...\n\n')
lados = [['Nome:', 'Lado:', 'Pistas:'], ['Vinícius', '?', ''], ['Alessandro', '?', ''], ['Marco Paludo', 'General da CIA dentro da PUC', ''], ['Professora Rafaela', 'Espiã da CIA', ''], ['Daniel Nowak', '?', ''], ['André Delphino', 'Espião da KGB', ''], ['Giulia Carvalho', '?', ''], ['Sheila Reinehr', 'Espiã da CIA', '']]



while True: 
  print(tabulate(lados,headers='firstrow', tablefmt='grid'))
  while True: 
    nomes = [['Código', 'Nome', 'Código', 'Nome'],['1', 'Vinícius', '2', 'Alessandro'], ['3', 'Marco Paludo', '4', 'Professora Rafaela'],['5', 'Daniel Nowak', '6', 'André Delphino'], ['7','Giulia Carvalho', '8', 'Sheila Reinehr']]
    armas = [['Código', 'Arma'], ['1', 'Fita Cassete'], ['2', 'Canivete Suíço'], ['3','Agulha'], ['4','Compasso'], ['5', 'Machado']]
    locais = [['Código','Locais suspeitos'], ['1','Sala dos monitores'], ['2', 'Biblioteca'], ['3', 'Sala secreta da CIA'], ['4', 'Ponte Escola\nPolitécnica']]
    escolhas_possiveis = [['Número da ação','Ação'], ['1','Investigar'], ['2', 'Acusar'], ['3', 'Consultar possibilidades']]
    print(tabulate(escolhas_possiveis, headers='firstrow', tablefmt='grid'))
    option = str(input('Digite sua escolha: ')).upper()
    if option =='3' or option in 'CONSULTAR':
      print('+'+'-'*90+'+')
      print('+--SUSPEITOS--+')
      print(tabulate(nomes,headers='firstrow', tablefmt='grid'))
      print(tabulate(armas,headers='firstrow', tablefmt='grid'))
      print(tabulate(locais,headers='firstrow', tablefmt='grid'))
      print('+'+'-'*90+'+')
      break
    elif option == '1' or option == 'INVESTIGAR':
      print('-'*len('INVESTIGAÇÃO')+'\nINVESTIGAÇÃO\n'+'-'*len('INVESTIGAÇÃO'))
      print(tabulate(nomes, headers='firstrow', tablefmt='grid'))
      while True:
        try: 
          p = int(input('Digite o número de quem deseja investigar: '))
          if p not in range(1,9):
            print('\033[31m\nDigite apenas opções válidas\n\033[m')
          else:
            break
        except:
          print('\033[31m\nDigite apenas opções válidas\n\033[m')
      if p == 1:
        print('\n\nVocê chega para investigar Vinícius...\n\n')
        time.sleep(1.5)
        print('Vinícius é encontrado morto na sala de monitores. Alguém o atingiu com um machado. Vinícius segurava uma foto do campûs com uma ponte circulada em vermelho.')
        time.sleep(1)
        lados[1][0] += '\n--- MORTO DURANTE INVESTIGAÇÃO ---'
        lados[1][2] = 'Mapa da PUCPR ponte marcada\nMorto com machado'
      elif p == 2:
        while True:
          try: 
            print('\nAlessadro:')
            time.sleep(2)
            opt = int(input('[1] - Seguir\n[2] - Interrogar\nSua escolha: '))    
            if opt not in range(1,3):
                print('\033[31m\nDigite apenas opções válidas\n\033[m')
            else: 
              break
          except:
              print('\033[31m\nDigite apenas opções válidas\n\033[m')
        if opt == 1:
          print('Você segue Alessandro e vê ele chegando próximo da Daniel Nowak, estudante de BCC.\n\nEles começam a conversar em alemão.')
          print('Você consegue se lembrar apenas da frase "Ich habe sie nicht ermordet".')
          time.sleep(5)
          while True:
            try:
              trans = int(input('O que deseja fazer?\n[1] - Traduzir "Ich habe sie nicht ermordet"\n[2] - Seguir em frente\nSua escolha: '))
              if trans not in range(1,3):
                print('\033[31m\nDigite apenas opções válidas\n\033[m')
              else: 
                if trans == 2:
                  break
                elif trans ==1: 
                  print('"Ich habe sie nicht ermordet" = "Eu não a matei"')
                  lados[2][2]+='"Eu não a matei."'
                  time.sleep(3)
                  break
            except:
              print('\033[31m\nDigite apenas opções válidas\n\033[m')
        elif opt ==2: 
          print('Ele é difícil de desembuchar, provavelmente recebeu treinamento para isso\n\nA única coisa que diz: "Quem a matou tinha treinamento. Foi com uma arma de pequeníssimo porte, pois no corpo há apenas uma marca de perfuração. Provavelmente, coisa da KGB."')
          lados[2][2]+='"Isso é coisa da KGB"\nAlessandro é um provável espião.'    
          lados[2][1] ="(Espião da CIA) v (Espião da KGB)"
          time.sleep(10)  
      elif p == 3:
            print('\nMarco paludo é conhecido como a Águia Careca nos corredores da PUCPR. Tem autorização especial para carregar armas no pátio.')
            while True:
                  try:
                    opt = int(input('[1] - Seguir\n[2] - Pedir informações sobre o assassinato\nSua escolha: '))
                    if opt not in range(1,3):
                      print('\033[31m\nDigite apenas opções válidas\n\033[m')
                    else: 
                      if opt==1: 
                        print('\nPaludo vai andando até o bloco amarelo. Bloco de humanas. Ele anda pelos corredores, uma névoa estranha preenche o ambiente, você escuta risos e vê pessoas fazendo poucas coisas e tocando violão.\nEle ingressa em uma sala. A névoa mais densa do que nunca, as risadas mais fortes.\nOlhando pela janela da sala, você vê ele mexendo no projetor de uma sala vazia.\nDe repente, de uma estante de livros, surge uma porta, uma sala secreta.')
                        time.sleep(15)
                        print('Você espera até ele sair para entrar e investigar a sala.')
                        time.sleep(5)
                        print('Ao entrar na sala. Você vê todos os tipos de armamento, inclusive um machado sujo de sangue.\nVocê encontra documentos sigilosos, um deles escrito: "Um agente duplo descoberto. Missão: Assassinar Daniel Nowak e queimar suas informações.\n\nRelatório do assassinato de Andreia Malucelli: O responsável trabalhava para o governo americano."\n\nO resto da mensagem havia sido censurado.\n\n')
                        print('Uma foto da Decâna na sala secreta da CIA é achada.')
                        time.sleep(20)
                        lados[3][2] = 'O assassino trabalhava no governo americano' + '\nFoto da decâna na sala secreta da CIA'
                        lados[5][1] = '(Espião da CIA) ^ (Espião da KGB)'
                      elif opt ==2:
                          print('\n"Não posso falar sobre o assassinato da Decâna. Mas sei que o único que é neutro é o Vinícius...\nA professora Kelly Rafaela sabe mais sobre o assassino, e ela pode lhe falar sobre o ocorrido."')
                          lados[1][1] = 'Neutro.'   
                          time.sleep(3)
                      break
                  except:
                    print('\033[31m\nDigite apenas opções válidas\n\033[m')
      elif p == 4:
            print('Professora Rafaela.')
            print('A única coisa que posso dizer, é que o assassino usou um objeto pontiagudo pequeno... E... nem devia dizer isso! O espião é agente duplo.')
            time.sleep(5)
            lados[4][2]= 'Objeto pequeno / Assassino é espião duplo'
      elif p ==5:
        print('Daniel Nowak... O estudante com passado obscuro.\n')
        print('Você segue Daniel, e vê ele roubando documentos da sala secreta da CIA, e indo até a sala dos monitores.')
        print('Lá, ele e André Delphino entram na sala. Você observa por cima da janela. Consegue escutar André dizendo "Não acredito que vou ter que matar a Giulia. Como ela poderia trabalhar para os EUA!"')
        print('DANIEL: "Cuidado, ela anda sempre armada com uma arma de pequeno porte para não chamar a atenção."')
        time.sleep(8)
        lados[7][1] = 'Espiã da CIA'
        lados[5][2] = 'André vai tentar matar a Giulia.\nGiulia possui sempre uma arma pequena'
      elif p == 6:
            print('André Delphino, o Carniceiro de Moscou.\nEle não colaboraria normalmente. Por isso você teve que sequestrar ele.')
            print('Depois de colocar um saco na cabeça dele e arrastá-lo até a biblioteca. Você o amarra a uma das cadeiras e começa o interrogatório. Após uma hora de perguntas... Ele só admite uma coisa: ')
            print('"A Sheila Reinehr sabe quem cometeu o crime!"\n"Eu conversei sobre isso apenas com o Alessandro"')
            time.sleep(8)
            lados[6][2] = 'Sheila sabe quem é o responsável\nAlessandro conversa com a KGB.'
      elif p == 7:
            print('Giulia Carvalho...')
            print('Foi difícil encontrar Giulia, você a viu saindo do ateliê de Arquitetura, aparentemente ela estava escondida lá. Com movimentos rápidos e diretos ela se movimenta pelo campus. Em um determinado momento, ela se esconde, e sai com o que parece ser um disfarce e escutando uma fita cassete.')
            print('Ela parece não querer contato com ninguém. Você é obrigado a tomar medidas drásticas.')
            print('Você enconta uma arma na cintura dela, e aponta para uma das salas. O semblante de frustração é claro.')
            print('GIULIA: "O André acha que eu fui responsável pelo assassinato da Decana. Por isso está vindo atrás de mim."')
            print('INVESTIGADOR: "O que você está escutando nessa fita? "')
            print('GIULIA: O hino da Alemanha Oriental. Preciso me preparar psicológicamente para um interrogatório seguido de tortura da KGB.')
            print('GIULIA: Olha, eu realmente preciso ir... Mas posso te dizer que o responsável por isso é mais inocente do que você imagina.')
            time.sleep(25)
            lados[7][2] = '"O responsável é mais inocente que pensamos"\n/ Fita Alemanha oriental / Sala de Arquitetura'
      elif p==8: 
        print('Sheila Reinehr...')
        print('Sheila decide colaborar parcialmente com o caso...\n')
        print('SHEILA: Vou lhe ajudar, mas não posso lhe dizer tudo por questões de segurança minha e sua. Entendo que as investigações podem fazer você chegar a conclusões ambíguas...') 
        print('Você precisa saber que o responsável por isso, está correndo muito perigo. Os planos da bomba de hidrogênio foram destruídos. Soviéticos e Americanos queriam a cabeça da decana, mas ninguém podia assassiná-la, pois apenas ela, se lembrava do projeto. Quem a matou cometeu um erro imperdoável.\n')
        time.sleep(15)
        print('SHEILA: "Eu entreguei vários documentos para o Alessandro essa semana sobre o caso. Aparentemente o que a matou não foi o corte, mas sim a queda no rio, em que ela fraturou o pescoço. Uma das nossas agentes infiltradas na KGB está em perigo por causa deste caso."')
        time.sleep(10)
        print('O telefone de Sheila toca no meio da conversa. Ela diz que é o Paludo.') 
        time.sleep(8)
        print('Sheila larga o telefone no chão COMPLETAMENTE PÁLIDA.')
        time.sleep(5)
        print('SHEILA: "Era o Paludo... Ele acha que Alessandro ou Giulia trabalham para a KGB."')
        time.sleep(5)
        print('SHEILA: "Não sabemos se são espiões duplos, ou se são infiltrados. Quantos documentos eles tiveram acesso! Que tragédia!"')
        time.sleep(4)
        lados[8][2] = 'Ela não foi morta pelo corte, e sim pela queda\nAlessandro recebe documentos da CIA\nAgente da CIA na KGB corre perigo\nAlessandro ou Giulia podem ser espiões duplos.'
        lados[7][1] = '(Espiã da CIA) v (Espiã da KGB)'
      break
    elif option == '2' or option == 'INVESTIGAR':
      result_set = [False,False, False]
      print(tabulate(nomes, headers='firstrow', tablefmt='grid'))
      opt_1 = str(input('\nDigite o código ou o nome de quem deseja acusar: ')).upper()
      if opt_1 == '7' or opt_1 in 'GIULIA CARVALHO':
        result_set[0] =True
      else: 
          result_set[0] = False
    print(tabulate(armas,headers='firstrow', tablefmt='grid'))
    opt_2 = str(input('\nDigite o código ou o nome da arma que cometeu o crime: ')).upper()
    if opt_2 == '4' or opt_2 in 'COMPASSO':
        result_set[1] = True
    else: 
          result_set[1] = False
    print(tabulate(locais,headers='firstrow', tablefmt='grid'))
    opt_3 = str(input('Digite o local onde acha que ocorreu o assassinato: ')).upper()
    if opt_3 == '4' or opt_3 in 'PONTE':
        result_set[2]=True
    else: 
          result_set[2] = False
    while True:
        print('Analisando suas escolhas...')
        if  (result_set[0] and result_set[1] and result_set[2]) == True:
            print('Você conseguiu!\nAo desobrir que a decâna sabia do seu envolvimento tanto com a CIA como a KGB, Giulia Carvalho, agente dupla foi ao seu encontro na ponte que dá acesso à Escola Politécnica da PUCPR\n')
            time.sleep(10)
            print('DECÂNA: Eu não posso deixar você fazer isso. Você corre perigo!')
            time.sleep(5)
            print('GIULIA: Não posso deixar a bomba de hidrogênio cair nas mãos dos Soviéticos, e para isso, ninguém pode saber do meu involvimento com a KGB.')
            time.sleep(5)
            print('DECÂNA: O projeto da bomba de hidrogênio previa a construção de usinas mais sustentáveis, nunca de armas mais letais. Eu queimei o projeto e joguei ele em uma lixeira. Embarco hoje de madrugada para a Suíça, lá, poderei me esconder dos dois lados')
            time.sleep(10)
            print('GIULIA: COMO')
            time.sleep(3)
            print('GIULIA: ASSIM?')
            time.sleep(3)
            print('DECÂNA: Corra Giulia, eu já consigo ver o André. \nCorra antes que seja tarde. Nessa bolsa tem tudo o que você precisa para fugir do país!')
            time.sleep(10)
            print('GIULIA: Você não me deu outra escolha... Eu não posso ser descoberta!')
            time.sleep(5)
            print('DECÂNA: Você não precisa fazer isso... Eles ainda vão descobrir sua identidade!')
            time.sleep(10)
            print('Giulia acerta a jugular da decâna com um compasso que guardava no bolso e a empurra da ponte.\nAndré, ainda confuso, foge e não ajuda Giulia a limpar os rastros')
            time.sleep(8)
            print('Giulia tinha tudo preparado para mudar sua identidade e ir morar na Suíça. Quanto remorço ela carregaria no seu coração. Ainda com lágrimas no rosto, ela é exposta.\n\n')
            time.sleep(10)
            print('Enquanto era algemada, ela contava tudo o que sabia a imprensa. Como Marco Paludo era o responsável pela morte de Vinícius Kuchnir, como estava sendo perseguida por outro agente duplo, Alessandro Schmidt, cujo plano inicial era entregar a bomba de Hidrogênio a quem oferecesse mais dinheiro.\n')
            sub_ = pyfiglet.figlet_format('CONSEGUIU! VINGOU A MORTE DA DECANA!', font='standard')
            print(sub_)
            break
        else:
            print(f'\nSua investigação é falha. Corra antes que o tempo acabe.\nVocê sabe {result_set.count(True)}/3 informações corretas.')
            break
    if (result_set[0] and result_set[1] and result_set[2]) == True:
          break
  if (result_set[0] and result_set[1] and result_set[2]) == True:
        break
