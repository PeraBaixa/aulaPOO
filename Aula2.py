PI = 3.14
"""
def circulo(raio):
    circun = 2*PI*raio
    area = (raio**2)*PI

    print(f"O círculo de raio {raio} centímetros tem:")
    print(f"- {circun} cm como circunferência")
    print(f"- {area} cm quadrados como área")
"""

class Circulo:
    def __init__(obj, raio):
        obj.raio = raio
        obj.circ = 2*PI*raio
        obj.area = (raio**2)*PI

    def __str__(obj):
        info = f"O círculo de raio {obj.raio} centímetros tem:\n"
        info += f"- {obj.circ} centímetros de circunferência\n"
        info += f"- {obj.area} centímetros quadrados de área"

        return info

raio = 0
while True:
    raio = input("Informe o comprimento do raio do círculo (cm): ")
    if raio.isnumeric():
        raio = int(raio)
        if int(raio) > 0:
            break
    print("O raio precisa ser um número e precisa ser maior que zero.")

print(Circulo(raio))
