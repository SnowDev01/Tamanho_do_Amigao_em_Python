import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Wedge
import random

entrada = input("Digite o tamanho do seu amigo em cm (use ponto ou vírgula): ")
entrada = entrada.replace(",", ".")
altura_usuario = float(entrada)

medias = [10, 13, 15, 17, 19, 23]

largura = 1
cor_medias = "#1E90FF"  # azul
cor_usuario = "#FF0000"  # vermelho

fig, ax = plt.subplots(figsize=(12,6))

posicoes_medias = [i * 3 for i in range(len(medias))]

for i, altura in enumerate(medias):
    x = posicoes_medias[i]
    y = 0

    retangulo = Rectangle((x, y), largura, altura - largura/2, color=cor_medias, ec="black")
    ax.add_patch(retangulo)
    
    meia_elipse = Wedge((x + largura/2, y + altura - largura/2), largura/2, 0, 180, facecolor=cor_medias, edgecolor="black")
    ax.add_patch(meia_elipse)
    
    ax.text(x + largura/2, y + altura + 0.3, f"{altura} cm", ha='center', va='bottom', fontsize=10)

# posição proporcional do usuário
min_media = min(medias)
max_media = max(medias)

if altura_usuario <= min_media:
    x_usuario = posicoes_medias[0] - (3 * (min_media - altura_usuario) / (max_media - min_media))
elif altura_usuario >= max_media:
    x_usuario = posicoes_medias[-1] + (3 * (altura_usuario - max_media) / (max_media - min_media))
else:
    for j in range(len(medias)-1):
        if medias[j] <= altura_usuario <= medias[j+1]:
            delta = (altura_usuario - medias[j]) / (medias[j+1] - medias[j])
            x_usuario = posicoes_medias[j] + delta * (posicoes_medias[j+1] - posicoes_medias[j])
            break

y_usuario = 0

retangulo_usuario = Rectangle((x_usuario, y_usuario), largura, altura_usuario - largura/2, color=cor_usuario, ec="black")
ax.add_patch(retangulo_usuario)

meia_elipse_usuario = Wedge((x_usuario + largura/2, y_usuario + altura_usuario - largura/2), largura/2, 0, 180, facecolor=cor_usuario, edgecolor="black")
ax.add_patch(meia_elipse_usuario)

ax.text(x_usuario + largura/2, y_usuario + altura_usuario + 0.3, f"Você: {altura_usuario} cm", ha='center', va='bottom', fontsize=10)

# Legenda
ax.text(posicoes_medias[-1]+1.5, max(max(medias), altura_usuario)/2, "Azul: Médias\nVermelho: Você", color="black", fontsize=12, bbox=dict(facecolor="white", alpha=0.8))

# Mensagens aleatórias dependendo do valor
if altura_usuario >= 18:
    mensagens = [
        "Irmão!! que que isso !!!!",
        "kkk tromba de nós todos",
        "Olha o tamanho cara!! kkkk",
        "Você foi agraciado, parabéns",
        "Muito Based você",
        "SIGAAAAAAAAAAAAAAA",
        "Chamam você de Alargador de Escapamento de Carro"
    ]
elif 10 <= altura_usuario <= 17:  # <- aqui cobrimos 10 a 17
    mensagens = [
        "Bem ... é isso ai, continue firme!",
        "Massa, tá de boa!",
        "Você consegue !!",
        "Lembre-se... você ainda é amado, vai ser amado",
        "Isso não é a única coisa que te define",
        "Olha que legal, 'amigão' tamanho médio, parabéns campeão",
        "Você ainda vai arrumar uma namorada um dia, relaxa!",
        "Nada mal, continue crescendo kkk",
        "... aposto que vai crescer mais, relaxa ;)"
    ]
else:  # altura_usuario <= 9
    mensagens = [
        "Só resta o Churascamento",
        "It's over",
        "Foi mogado pelo chat",
        "F no Chat",
        "Sobrou nada pro betinha... mas um dia vai!",
        "Oh Lee...",
        "My way - Frank Sinatra (3:07) ... só escuta",
        "Esquece amigo ... esquece"
    ]

mensagem = random.choice(mensagens)
ax.text(posicoes_medias[-1]/2, -2, mensagem, ha='center', va='top', fontsize=12, color="purple")

ax.set_xlim(-2, posicoes_medias[-1]+4)
ax.set_ylim(-3, max(max(medias), altura_usuario)+3)
ax.set_xticks(posicoes_medias)
ax.set_xticklabels([f"Média {i+1}" for i in range(len(medias))])
ax.set_ylabel("Tamanho em cm")
ax.set_title("Comparação das Médias com Você (Proporcional)")

plt.show()

