# Personagens
define vm = Character("Voz Masculina Desconhecida", color="#00aaff")
define vf = Character("Voz Feminina Desconhecida", color="#ff66cc")
define m  = Character("Mariana", color="#ffcc00")
define a  = Character("Akiara", color="#cc66ff")
define g  = Character("Gustavo", color="#00ff00")
define l  = Character("Lucas", color="#ff6600")
define b  = Character("Beathriz", color="#ff3399")
define d  = Character("Diretor", color="#999999")
define p  = Character("[player_name]", color="#ffffff")

# Protagonista
default player_name = ""

# Variáveis de amizade
default friendship_mariana = 0
default friendship_akiara = 0
default friendship_gustavo = 0
default friendship_lucas = 0
default friendship_beathriz = 0

# Início do jogo
label start:

    label cap_0:
        scene black with fade

        "{cps=40}."
        "{cps=40}.."
        "{cps=40}..."
        "{cps=40}ah !"
        "{cps=40}Olá querido jogador !"
        "{cps=40}É um prazer ter você aqui"
        "{cps=40}Antes de começar, preciso avisar que este jogo apresenta conteúdo para maiores, além de conteúdo sensível que possa gerar gatilho em algumas pessoas."
        "{cps=40}Você ainda pretende jogar o jogo sabendo disso ?"

        menu:
            "{cps=40}Sim":
                "{cps=40}Tudo bem."
                "{cps=40}Gostaria de saber o que vem por aí ?"
                menu:
                    "{cps=40}Sim":
                        "{cps=40}Certo ..."
                        "{cps=40}O jogo apresenta ..."
                        "{cps=40}Cenas de violência"
                        "{cps=40}Cenas de abuso verbal"
                        "{cps=40}Cenas de abuso físico"
                        "{cps=40}Cenas de abuso sexual"
                        "{cps=40}Cenas de abuso psicológico"
                        "{cps=40}Cenas de automutilação"
                        "{cps=40}Cenas de suicídio"
                        "{cps=40}Cenas de bullying"
                        "{cps=40}Cenas de assédio"
                        "{cps=40}Cenas de preconceito"
                        "{cps=40}Cenas de uso de drogas lícitas e ilícitas"
                        "{cps=40}Cenas de álcool"
                        "{cps=40}Cenas de tabaco"
                        "{cps=40}Cenas de transtornos mentais"
                        "{cps=40}Cenas de doenças graves"
                        "{cps=40}Cenas de morte"
                        "{cps=40}Cenas de traumas infantis e familiares"
                        "{cps=40}Entre outros tópicos ..."
                        "{cps=40}Este jogo não chega a ser um Hentai, mas possui abordagens de temas relacionados."
                        "{cps=40}Com isso ciente ..."
                        "{cps=40}Podemos começar"
                        "{cps=40}..."
                        "{cps=40}Você REALMENTE tem certeza que quer jogar ainda ciente disso ? ..."

                        menu:
                            "{cps=40}Sim":
                                "{cps=40}Ok ..."
                                "{cps=40}Eu tentei ..."
                                jump cap_0_1
                            "{cps=40}Não":
                                "{cps=40}Tudo bem, se você não se sente confortável, pode fechar o jogo agora."
                                return

                    "{cps=40}Não":
                        "{cps=40}Certo ..."
                        "{cps=40}Podemos começar a jogar"
                        jump cap_0_1

            "{cps=40}Não":
                "{cps=40}Tudo bem, se você não se sente confortável, pode fechar o jogo agora."
                return

    label cap_0_1:

        # MOSTRAR UM VÍDEO DO INICIO DO JOGO COM UMA FIGURA FEMININA REINICIANDO O COMPUTADOR

        $ player_name = renpy.input("{cps=40}Qual é o seu nome?")
        $ player_name = player_name.strip()

        scene bg room with fade

        p "{cps=40}."
        p "{cps=40}.."
        p "{cps=40}..."
        p "{cps=40}Ai-ai..."
        p "{cps=40}Dormir demais ..."
        p "{cps=40}aff ... queria dormir mais"
        p "{cps=40}..."
        p "{cps=40}Ainda bem que estou de férias"
        p "{cps=40}acho que posso dormir mais um pouco e..."
        "{cps=40}7:34 AM"
        p "{cps=40}normal, ainda ta cedo, deixa eu ver que dia é hoje ..."
        p "{cps=40}."
        p "{cps=40}.."
        p "{cps=40}..."
        p "{cps=40}n"
        p "{cps=40}n-na-não to acreditando ..."
        p "{cps=40}é dia 18 de janeiro"
        p "{cps=40}EU ESTOU ATRASADO !!!"
        p "{cps=40}Droga, droga, droga !"
        p "{cps=40}Ai Meu Deus !"
        p "{cps=40}AI-AI universo !!"
        p "{cps=40}Eu tenho que me arrumar rápido !"
        p "{cps=40}Eu tenho que correr !"
        "{cps=40}Me arrumo ligeiramnete para a escola e saio correndo de casa "
        "{cps=40}Hoje é meu primeiro dia de aula no ensino médio"
        "{cps=40}Hoje é o dia em que eu mudo tudo, vou deixar de ser o garoto solitário com poucos amigos que eu era no ensino fundamental todo Nerdola e Capenga"
        "{cps=40}Hoje é o dia em que eu começo a minha nova vida !"
        "{cps=40}Vou pegar um monte de mina"
        "{cps=40}Conseguir entrar em projetos com os professores"
        "{cps=40}E fazer um monte de amigos"
        "{cps=40}Posso ate pegar um Intercambio quem sabe "
        "{cps=40}Chego no Terminal para pegar o onibus e eu adentro o veiculo"
        "{cps=40}O onibus está cheio, mas eu consigo um lugar para sentar"
        "{cps=40}É imprecionante quanta gente tem de 7 da manhã indo trabalhar, estudar ou vagabunda por ai"
        "{cps=40}impresionante que pelomenos alguem aqui deve ta indo para um dite no parque com alguma gata ... aff queria uma namorada"
        "{cps=40}* O onibus segue seu trajeto *"
        "{cps=40}."
        "{cps=40}.."
        "{cps=40}..."
        vm "{cps=40}Lisença "
        vm "{cps=40}Posso sentar aqui ?"
        vm "{cps=40}PERA !!!"
        vm "{cps=40}SÓ PODE SER MENTIRA MANO"
        vm "{cps=40}É tudo [player_name]?"
        
    return
