from abc import ABC, abstractmethod

#Classe para contaBanco()
class ContaBancaria:
    def __init__(obj, titular, saldoInicial):
        obj.titular = titular
        obj.__saldo = saldoInicial

    def depositar(obj, valor):
        if valor > 0:
            obj.__saldo += valor
            ContaBancaria.__registrarOperacao("Depósito")

            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    def retirar(obj, valor):
        if valor > 0 and obj.__saldo >= valor:
            obj.__saldo -= valor
            ContaBancaria.__registrarOperacao("Decremento de saldo")
        else:
            print("Valor inválido para a operação")

    @staticmethod
    def __registrarOperacao(tipo):
        print(f"Log interno: Operação de {tipo} registrada no sistema.")

    def consultarSaldo(obj):
        return f"Saldo atual de {obj.titular}: R${obj.__saldo:.2f}"

#Classes para emissor()
class Bichos(ABC):
    
    @abstractmethod
    def emitirSom(obj):
        pass
    
    @abstractmethod
    def dormir(obj):
        pass

    @abstractmethod
    def fazerCarinho(obj):
        pass

class Cachorro(Bichos):
    def emitirSom(obj):
        return "Au au!"

    def dormir(obj):
        return "*Faz várias voltas antes de dormir*"

    def fazerCarinho(obj):
        return "*Dá várias lambidas*"

class Gato(Bichos):
    def emitirSom(obj):
        return "Miau miau!"

    def dormir(obj):
        return "*Só dorme quando quer, onde quer*"
    
    def fazerCarinho(obj):
        return "*Dá cabeçadas*"

class Radio:
    def emitirSom(obj):
        return "*Musiquinha maneira*"

#Classe para calculadora()
class Calculadora:
    def calcularArea(obj, ladoA, ladoB=None):
        if ladoB:
            print(f"Área do retângulo: {ladoA} X {ladoB} = {ladoA * ladoB}")
        else:
            area = ladoA
            print(f"Área do quadrado: {ladoA} vezes a si mesmo = {ladoA ** 2}")

def main():
    print("1 - Conta Bancária")
    print("2 - Emissores de som")
    print("3 - Calculadora")
    while True:
        match input("Escolha qual programa deseja testar: "):
            case "1":
                print("Você selecionou \"Conta Bancária\"\n")
                contaBanco()
            case "2":
                print("Você selecionou \"Emissores de Som\"\n")
                emissor()
            case "3":
                print("Você selecionou \"Calculadora\"\n")
                calculadora()
            case __:
                print("Valor inválido.")
                continue

        if input("Deseja continuar testando os programas? (s/n) ").lower() != "s":
            break

def contaBanco():
    minhaConta = ContaBancaria("Antonio", 1000.00)
    
    val = None
    while True:
        print(minhaConta.consultarSaldo())

        try:
            val = int(input("Informe o valor da operação (0 para sair): "))
            if val == 0: break
        except:
            print("O valor inserido deve ser um número")
        else:
            print("1 - Depósito")
            print("2 - Retirada")
            match input("Informe a operação desejada: "):
                case "1":
                    minhaConta.depositar(val)
                case "2":
                    minhaConta.retirar(val)
                case __:
                    print("Valor não identificado.")
    print("Até mais!\n")

def emissor():    
    barulhos = [Cachorro(), Gato(), Radio()]

    for coisa in barulhos:
        print(f"O som emitido é: {coisa.emitirSom()}")
        try:
            print(coisa.dormir(),"\n", coisa.fazerCarinho())
        except:
            print("Infelizmente, rádios não são bichos")

    print()

def calculadora():
    calc = Calculadora()
    calc.calcularArea(10)
    calc.calcularArea(10, 5)

    print()

if __name__ == "__main__":
    main()
