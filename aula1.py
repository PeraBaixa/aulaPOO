class Fusca:
    def __init__(obj, renavan, placa, rodas, carroc, motor, cor, anofabr, modelo, quilom=0, tanq=0):
        obj.renavan = renavan
        obj.placa = placa
        obj.rodas = rodas #diâmetro das rodas, de 15 a 18 polegadas
        obj.carroc = carroc #fastback ou conversível (os dois 2 portas)
        obj.motor = motor #de 1,2L até 1,6L F4
        obj.cor = cor #vermelho, azul, amarelo ou verde
        obj.anofabr = anofabr
        obj.modelo = modelo #De 65, 1600 S ou Itamar
        obj.quilom = quilom
        obj.tanq = (tanq if tanq >= 0 and tanq <= 100 else 0)
        obj.direc = None

    
    def __str__(obj):
        orient = ""
        match obj.direc:
            case 2:
                orient = "norte"
            case 1:
                orient = "oeste"
            case 3:
                orient = "leste"
            case 4:
                orient = "sul"
            case __:
                orient = "parado"

        lista = "Lista de características:\n"
        lista += f"* Renavan: {obj.renavan}\n"
        lista += f"* Placa: {obj.placa}\n"
        lista += f"* Diâmetro das rodas: {obj.rodas} polegadas\n"
        lista += f"* Carroceria: {obj.carroc}\n"
        lista += f"* Motor {obj.carroc}L F4\n"
        lista += f"* Cor: {obj.cor}\n"
        lista += f"* Ano de fabricação: {obj.anofabr}\n"
        lista += f"* Modelo: {obj.modelo}\n"
        lista += f"* Quilometragem: {obj.quilom} quilômetros\n"
        lista += f"* Tanq: {obj.tanq}%\n"
        lista += ("* Ele está "+("parado\n" if not obj.direc else f"indo para {orient}\n"))

        return lista

    def andar(obj):
        if not obj.direc:
            obj.direc = 2
        else:
            "O carro já está andando!"
    
    def virar(obj, lado="direita"):
        if obj.direc:
            if lado == "direita":
                obj.direc += 1
            else:
                obj.direc -= 1
            
            if obj.direc > 4:
                obj.direc = 1
            if obj.direc < 1:
                obj.direc = 4
        else:
            print("O carro está parado!")

    def parar(obj):
        obj.direc = None

fuscas = [
   Fusca("3de3", "pyr3jor", 15, "fastback", 1.4, "verde", 2001, "65", 500, 50),
   Fusca("rtyu", "tgy7poi", 17, "fastback", 1.2, "azul", 2026, "Itamar", 0, 0),
   Fusca("u64p", "hjk3prw", 18, "Conversível", 1.5, "amarelo", 1991, "1600 S", 1500, 100)
]
[print(f) for f in fuscas]
