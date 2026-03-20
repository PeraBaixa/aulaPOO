from random import randint

def main():
    print("1 - Jogo da Forca")
    print("2 - Jogo das Vogais")
    print("3 - Encriptador")
    opt = input("Dentre as opções na lista, escolha uma para testar: ")

    match opt:
        case "1":
            print("\n-------------------------------")
            print("Você selecionou o Jogo da Forca")
            print("-------------------------------")
            jogoDaForca()
        case "2":
            print("\n----------------------------------")
            print("Você selecionou o Jogo das vogais")
            print("----------------------------------")
            jogoDasVogais()
        case "3":
            print("\n------------------------------")
            print("Você selecionou o Encriptador")
            print("------------------------------")
            encriptador()
        case __:
            print("Resposta inválida")

def jogoDaForca():
    lista = [
        "cinco",
        "lerdo",
        "jumbo",
        "prima",
        "guria",
        "horta",
        "navio",
        "irmao",
        "lapis",
        "abaco"
    ]

    dicas = [
        "Um número cuja quantidade de letras é igual ao seu valor",
        "Um homem que não é rápido",
        "Tamanho bem grande",
        "A filha de um irmão de um dos seu pais",
        "Como um gaúcho se refere a uma menina",
        "Onde se cultiva plantas",
        "Meio de transporte náutico",
        "Alguém que foi parido pelos os seus pais, mas que não é você",
        "Ferramenta usada para escrever",
        "Ferramenta antiga usada para fazer cálculos"
    ]

    #O index do array, assim funciona tanto na lista quanto nas dicas
    alvo = randint(0, 9)

    #O quanto da palavra que já foi descoberto
    desc = "01234" #Algarismos representam a posição da letra

    pontos = 5

    while True:
        print(f"\nTentativas restantes: {pontos}")
        print("*******")
        print("*", end="")
        [(print("_", end="") if l.isdigit() else print(l, end="")) for l in desc]
        print("*")
        print("*******")
        if pontos <= 3: print(f"Dica: {dicas[alvo]}")

        chute = None
        while True:
            chute = input("Adivinhe uma letra: ").lower()
            if chute.isalpha() and len(chute) == 1:
                break
            else:
                print("Você deve adivinhar uma letra e apenas isso!")
        
        acertou = False
        for lugar, letra in enumerate(lista[alvo]):
            if letra == chute and desc[lugar].isdigit():
                acertou = True
                desc = desc.replace(str(lugar), letra)

        print("Você acertou!") if acertou else print("Você errou!")
        pontos -= 1

        if desc.isalpha():
            print("UFA!!! Você descobriu a palavra " + lista[alvo])
            break
        elif pontos == 0:
            print("FORCA!!! Você não descobriu a palavra " + lista[alvo])

def jogoDasVogais():
    while len(frase := input("Informe a frase: ")) > 20:
        print("Frase muito grande! Escreva outra!")

    vogais = [0, 0, 0, 0, 0]
    for letra in frase.lower():
        match letra:
            case "a": vogais[0] += 1
            case "e": vogais[1] += 1
            case "i": vogais[2] += 1
            case "o": vogais[3] += 1
            case "u": vogais[4] += 1

    print("Essas são as quantidades de cada vogal dentro da frase: ")
    print(f" A - {vogais[0]}")
    print(f" E - {vogais[1]}")
    print(f" I - {vogais[2]}")
    print(f" O - {vogais[3]}")
    print(f" U - {vogais[4]}")

def encriptador():
    while len(palavra := input("Digite a palavra a ser encriptada: ")) > 5 or not palavra.isalpha():
        print("Palavra muito grande ou contém valores que não letras")
    
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    encr = ""
    nums = [alfabeto.find(letra) for letra in palavra.lower()]

    for v in nums:
        encr += (alfabeto[v+1] if v+1 < 26 else "a")

    print(f"Palavra encriptada: {encr}")

main()
