from random import randint
def main():
    print("Escolha uma das seguintes opções de programas para testar: ")
    print("1 - Adivinhar um número")
    print("2 - Adivinhar um resultado")
    while True:
        op = input("Opção: ")

        match op:
            case "1":
                forca()
            case "2":
                forcaCalc()
            case __:
                print("Valor inválido!")
                continue
        
        if input("Quer testar algum programa novamente? (y/n) ").lower() != 'y':
            break

#Jogo da forca com adivinhação de números
def forca():
    print("\n____________________________________")
    print("Você selecionou Adivinhar um Número!")
    alvo = randint(1, 100)
    pontos = 5
    
    while True:
        print(f"Pontos atuais: {pontos}")
        chute = testaChute()
        
        if chute == alvo:
            print("UFA!!!")
            break
        elif pontos == 1:
            print("FORCA!!!")
            #print(alvo)
            break
        elif chute > alvo:
            print("DESCE!!!")
            pontos -= 1
        else:
            print("SOBE!!!")
            pontos -= 1

def testaChute():
    while True:
        chute = input("Adivinhe um número: ")
        try:
            chute = int(chute)
            if chute < 1 or chute > 100: (1/0) #Força um erro
        except:
            print("Valor inválido!")
            continue
        break
    
    return chute

#Jogo da forca com adivinhação do resultado de uma operação
def forcaCalc():
    print("\n____________________________________")
    print("Você selecionou Adivinhar um Resultado!")
    v1 = randint(2, 100)
    v2 = randint(1, (v1-1))
    oper = randint(0,1)
    res = None

    pontos = 5

    if oper:
        res = v1+v2
    else:
        res = v1-v2
    
    while True:
        print(f"Tentativas restantes: {pontos}")
        print(f"Valores gerados: '{v1}' e '{v2}'")
        chute = testaRes()

        if chute == res:
            print("UFA!!!")
            break
        elif pontos == 1:
            print("FORCA!!!")
            break
        
        print("ERROU!!!")
        pontos -= 1

def testaRes():
    while True:
        try:
            chute = int(input("Adivinhe o resultado: "))
        except:
            print("Resposta inválida!")
            continue
        break
    
    return chute

if __name__ == "__main__":
    main()
