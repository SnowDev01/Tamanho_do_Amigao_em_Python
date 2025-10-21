print("Olá, seja bem vindo ao Mundo de RPG em python\nVamos criar seu personagem:")
nome = input("Digite um nome: ")
idade_valida = False
while not idade_valida:
    idade_str = input("Digite uma idade: ")
    idade_valida_local = True
    for c in idade_str:
        if c < '0' or c > '9':
            idade_valida_local = False
            break
    if idade_valida_local and len(idade_str) > 0:
        idade = 0
        k = 0
        while k < len(idade_str):
            idade = idade * 10 + (ord(idade_str[k]) - ord('0'))
            k += 1
        idade_valida = True
    else:
        print("Idade inválida! Digite um número inteiro.")
dinheiro_valido = False
while not dinheiro_valido:
    dinheiro_str = input("Digite uma quantidade de Dinheiro: ")
    ponto = False
    digitos = 0
    dinheiro_valida_local = True
    for c in dinheiro_str:
        if c == '.' and not ponto:
            ponto = True
        elif c >= '0' and c <= '9':
            digitos += 1
        else:
            dinheiro_valida_local = False
            break
    if dinheiro_valida_local and digitos > 0:
        # conversão manual para float
        parte_inteira = 0
        parte_decimal = 0
        decimal = False
        casas_decimais = 0
        l = 0
        while l < len(dinheiro_str):
            if dinheiro_str[l] == '.':
                decimal = True
            elif not decimal:
                parte_inteira = parte_inteira * 10 + (ord(dinheiro_str[l]) - ord('0'))
            else:
                parte_decimal = parte_decimal * 10 + (ord(dinheiro_str[l]) - ord('0'))
                casas_decimais += 1
            l += 1
        if casas_decimais > 0:
            dinheiro = parte_inteira + parte_decimal / (10 ** casas_decimais)
        else:
            dinheiro = parte_inteira
        dinheiro_valido = True
    else:
        print("Valor inválido! Digite um número.")
print(f"===\nLegal!!!\nSeu personagem se chama {nome}, tem {idade} anos e saldo de {dinheiro} moedas\n===")
print("Agora vamos pensar como ele(a) é")
classes = [
    "Patrulheiro", "Bárbaro", "Monge", "Ladino", "Paladino", "Clérigo", "Mago", "Bruxo", "Feiticeiro", "Druida", "Bardo", "Artífice"
]
print("Qual classe você gostaria que seu personagem fosse?")
i = 0
while i < len(classes):
    print("- " + classes[i])
    i += 1
classe_valida = False
while not classe_valida:
    classe = input("Digite o nome da sua classe: ")
    j = 0
    while j < len(classes):
        if classe.capitalize() == classes[j]:
            print(f"Você escolheu a classe: {classe} 🗡️")
            classe_valida = True
            break
        j += 1
    if not classe_valida:
        print("Classe inválida! Tente novamente.")