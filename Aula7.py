from abc import ABC, abstractmethod

#LIVRO:
class Livro:
    """Crie uma classe que armazene o título, autor e as páginas lidas. 
    O saldo de páginas lidas deve ser privado e alterado apenas por
    um método de leitura que permite a atualização do número de 
    páginas lidas."""
    def __init__(obj, titulo, autor, pagsLidas):
        obj.titulo = titulo
        obj.autor = autor
        obj.__pagsLidas = pagsLidas
    
    def atualizaPags(obj, qunt=None):
        if qunt:
            obj.__pagsLidas += qunt
        else:
            obj.__pagsLidas = 0

def livro():
    l = Livro("Eu, Roberto Macedo", "Roberto Alburquerque", 30)
    try:
        print(f"{l.__pagsLidas} páginas já foram lidas")
    except:
        print("Não te interessa quantas páginas já foram lidas!")
        print(f"Dito isso, foram lidas {l._Livro__pagsLidas} páginas")

#TERMOMETRO:
class Termometro:
    """Modele um Termômetro que armazena a temperatura atual de
    forma privada e permite apenas leituras e ajustes via métodos."""
    __tempAtual = 35

    @classmethod
    def setTempAtual(cls, temp):
        cls.__tempAtual = temp

    @classmethod
    def getTempAtual(cls):
        return cls.__tempAtual

def termo():
    try:
        print(f"Nesse momento, está {Termometro.__tempAtual} graus celcius")
    except:
        print(f"Nesse momento, está {Termometro.getTempAtual()-1} graus celcius")
    
    print("Mas a temperatura mudou!")
    try:
        Termometro.__tempAtual = 31
    except:
        Termometro.setTempAtual(29)

    Termometro.setTempAtual(29)
    print(f"Agora, está {Termometro.getTempAtual()} graus celcius")

#PET:
class Animal:
    """Desenvolva uma classe para um animal de estimação com nome e 
    espécie. Use herança para criar uma subclasse Cachorro."""
    def __init__(obj, nome, raca):
        obj.nome = nome
        obj.raca = raca

class Cachorro(Animal):
    def __str__(obj):
        return f"O cachorro {obj.nome} é um {obj.raca}"

def pet():
    dog = Cachorro("Alberto", "York Shire")
    print(dog)

#CALCULADORA:
class Calculadora:
    """Crie uma classe Calculadora com métodos para as quatro
    operações básicas, sem atributos internos"""

    @staticmethod
    def soma(a, b):
        return a + b
    
    @staticmethod
    def subtracao(a, b):
        return a - b
    
    @staticmethod
    def multiplicacao(a, b):
        return a * b
    
    @staticmethod
    def divisao(a, b):
        return a / b

def calcula():
    print("Escolha dois números:")
    a = int(input("Valor 'A': "))
    b = int(input("Valor 'B': "))
    print("Escolha a operação:")
    print("+ - Soma")
    print("- - Subtração")
    print("* - Multiplicação")
    print("/ - Divisão")
    op = input("Operação: ")

    match op:
        case "+":
            res = Calculadora.soma(a, b)
        case "-":
            res = Calculadora.subtracao(a, b)
        case "*":
            res = Calculadora.multiplicacao(a, b)
        case "/":
            res = Calculadora.divisao(a, b)
        case __:
            print("Errou!")
            res = False

    if res:
        print(f"{a} {op} {b} = {res}")
        
#USUÁRIO:
class Usuario:
    """Modele uma classe Usuario onde a senha é um atributo privado
    e só pode ser alterada se o usuário informar a senha antiga
    corretamente"""

    def __init__(obj, nome, senha):
        obj.nome = nome
        obj.__senha = str(senha)
    
    def mudarSenha(obj):
        if input("Informe sua senha antiga: ") == obj.__senha:
            obj.__senha = input("Informe a nova senha: ")
            print("Senha mudada com sucesso!")
        else:
            print("Senha antiga incorreta")

def login():
    usu = Usuario("AAAAAAA", 989898)
    usu.mudarSenha()

#RELÓGIO DIGITAL:
class Tempo:
    """Crie uma classe que armazene horas e minutos. Impeça, via
    métodos, que o usuário defina uma hora maior que 23 ou minuto
    maior que 59"""

    def __init__(obj, horas, mins):
        obj.__horas = (horas if 0 <= horas <= 23 else 0)
        obj.__mins = (mins if 0 <= mins <= 59 else 0)

    def setHoras(obj, h):
        if 0 <= h <= 23:
            obj.__horas = h
        else:
            print("Valor inválido!")
    
    def setMins(obj, m):
        if 0 <= m <= 59:
            obj.__mins = m
        else:
            print("Valor inválido")
    
    def __str__(obj):
        return f"{obj.__horas}:{obj.__mins}"

def relogio():
    relog = Tempo(15, 8)
    relog.setHoras(25)
    relog.setMins(34)
    print(relog)

#CARRINHO:
class Carrinho:
    """Crie uma classe Produto e uma classe Carrinho que
    armazena uma lista de produtos e calcula o total."""
    def __init__(obj, prods):
        obj.prods = prods

    def calculaTotal(obj):
        a = 0
        for p in obj.prods:
            a += p.preco
        return a

class Produto:
    def __init__(obj, nome, preco):
        obj.nome = nome
        obj.preco = preco

def carrinho():
    carro = Carrinho([Produto("PC gamer", 40), Produto("Mouse", 70)])
    print(f"Total do carrinho: {carro.calculaTotal()}")

#CONTROLE DE ESTOQUE:
class Item:
    """Modele um item de estoque com nome e quantidade. A
    quantidade não pode ser negativa e deve ser protegida
    (privada)"""
    def __init__(obj, nome, qunt):
        obj.nome = nome
        obj.__qunt = (qunt if qunt >= 0 else 0)

    def setQunt(obj, qunt):
        if qunt >= 0:
            obj.__qunt = qunt
        else:
            print("Valor inválido!")

    def getQunt(obj):
        return obj.__qunt

def estoque():
    item = Item("paçoca", 80)
    item.setQunt(-15)
    print(f"Há {item.getQunt()} {item.nome}s em estoque")

#PAGAMENTOS DIVERSOS
class Pagamento(ABC):
    """Crie uma classe abstrata Pagamento com um método
    processar(). Implemente as subclasses Cartao e Boleto."""
    @abstractmethod
    def processar():
        pass

class Cartao(Pagamento):
    def processar(obj):
        print("O pagamento foi processado em cartão")

class Boleto(Pagamento):
    def processar(obj):
        print("O pagamento foi processado em boleto")

def paga():
    Cartao().processar()
    Boleto().processar()

#SISTEMA DE ALUGUEL
class Imovel(ABC):
    """Modele um sistema de aluguel de imóveis. Use abstração para
    Imovel e crie as especializações Casa e Apartamento com 2 regras
    de condomínio para a casa e 2 para o apartamento."""
    
    @abstractmethod
    def retornaRegras():
        pass

class Casa(Imovel):
    def retornaRegras(obj):
        print("Regras da casa:")
        print("1 - Tirar os sapatos antes de entrar")
        print("2 - Lavar a louça antes de sair")

class Apartamento(Imovel):
    def retornaRegras(obj):
        print("Regras do apartamento:")
        print("1 - Nunca sair com alguma janela aberta")
        print("2 - Comer apenas na cozinha")

def aluguel():
    Casa().retornaRegras()
    Apartamento().retornaRegras()

def main():
    opt = None
    while opt != 0:
        print("Dentre estas opções:")
        print("1 - Livro")
        print("2 - Termômetro")
        print("3 - Pet")
        print("4 - Calculadora")
        print("5 - Usuário")
        print("6 - Relógio digital")
        print("7 - Carrinho")
        print("8 - Controle de estoque")
        print("9 - Pagamentos diversos")
        print("10 - Sistema de aluguel")
        print("0 - Terminar o programa")
        
        try:
            opt = int(input("Escolha qual progrma deseja testar: "))
        except:
            print("Valor inválido!\n")
            continue
        
        s = "Você selecionou"
        match opt:
            case 1:
                print(f"{s} \"Livro\"\n")
                livro()
            case 2:
                print(f"{s} \"Termômetro\"\n")
                termo()
            case 3:
                print(f"{s} \"Pet\"\n")
                pet()
            case 4:
                print(f"{s} \"Calculadora\"\n")
                calcula()
            case 5:
                print(f"{s} \"Usuário\"\n")
                login()
            case 6:
                print(f"{s} \"Relógio digital\"\n")
                relogio()
            case 7:
                print(f"{s} \"Carrinho\"\n")
                carrinho()
            case 8:
                print(f"{s} \"Controle de estoque\"\n")
                estoque()
            case 9:
                print(f"{s} \"Pagamentos Diversos\"\n")
                paga()
            case 10:
                print(f"{s} \"Sistema de aluguel\"\n")
                aluguel()
            case __:
                opt = 0
        
        if opt != 0:
            print("Clique em enter para voltar ao menu de opções")
            input()

if __name__ == "__main__":
    main()
