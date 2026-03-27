from abc import ABC, abstractmethod
import math

import datetime

#CLASSES:
#Para carros():
class Carro:
    def __init__(obj, marca, modelo):
        obj.marca = marca
        obj.modelo = modelo
        obj.ligado = False

    def ligar(obj):
        if obj.ligado:
            print(f"{obj.modelo} já está ligado")
        else:
            obj.ligado = True
            print(f"{obj.modelo} ligou!")

    def desligar(obj):
        if obj.ligado:
            obj.ligado = False
            print(f"{obj.modelo} desligou!")
        else:
            print(f"{obj.modelo} já está desligado")

#Para formas():
class Forma(ABC):
    @abstractmethod
    def calcular_area(obj):
        pass

class Quadrado(Forma):
    def __init__(obj, lado):
        obj.lado = lado

    def calcular_area(obj):
        return obj.lado ** 2

class Circulo(Forma):
    def __init__(obj, raio):
        obj.raio = raio
    
    def calcular_area(obj):
        return math.pi * (obj.raio ** 2)

class Equilatero(Quadrado):
    def calcular_area(obj):
        return (super().calcular_area() * (3 ** 1/2))/4

#Para funcs():
class Funcionario:
    def __init__(obj, nome, salario):
        obj.nome = nome
        obj.salario = salario

    def exibir_dados(obj):
        print(f"Nome: {obj.nome} | Salário: R${obj.salario:.2f}")
    
class Gerente(Funcionario):
    def __init__(obj, nome, salario, bonus):
        super().__init__(nome, salario)
        obj.bonus = bonus

    def calcular_total(obj):
        total = obj.salario + obj.bonus
        print(f"Total com bônus: R${total:.2f}")

class Minion(Gerente):
    def __init__(obj, nome, salario, bonus):
        super().__init__(nome, salario, bonus)

#Para relogio():
class Relogio:
    def mostrar_hora(obj):
        return datetime.datetime.now().strftime("%H:%M:%S")

class Calendario:
    def mostrar_data(obj):
        return datetime.datetime.now().strftime("%d/%m/%Y")

class Smartwatch(Relogio, Calendario):
    def mostrar_tudo(obj):
        hora = obj.mostrar_hora
        data = obj.mostrar_data
        print(f"Smartwatch - Data: {data} | Hora: {hora}")

#Funções:
def main():
    while True:
        print("Escolha qual programa testar:")
        print("1 - Carros")
        print("2 - Formas")
        print("3 - Funcionários")
        print("4 - Relógio")

        match input("Opção: "):
            case "1":
                print("Você selecionou o programas dos carros\n")
                carros()
            case "2":
                print("Você selecionou o programas das formas\n")
                formas()
            case "3":
                print("Você selecionou o programas dos funcionários\n")
                funcs()
            case "4":
                print("Você selecionou o programas dos relógios\n")
                relogio()
            case __:
                print("Valor inválido")
        
        if input("Deseja continuar testando? (s/n) ").lower() == "s":
            continue
        else:
            break

def carros():
    meuCarro = Carro("Toyota", "Corolla")
    carroProf = Carro("Ford", "Mustang")

    meuCarro.ligar()
    meuCarro.ligar()
    meuCarro.desligar()

    carroProf.desligar()
    carroProf.ligar()
    carroProf.desligar()
    
def formas():
    formas = [
        Quadrado(4),
        Circulo(3),
        Equilatero(4)
    ]

    print("-- Relatório de Áreas --")
    [print(f"Área da forma: {f.calcular_area():.2f}") for f in formas]

def funcs():
    kevin = Minion("Kevin", 5000, 1500)

    kevin.exibir_dados()
    kevin.calcular_total()

def relogio():
    meuRelog = Smartwatch()
    meuRelog.mostrar_tudo()

if __name__ == "__main__":
    main()
