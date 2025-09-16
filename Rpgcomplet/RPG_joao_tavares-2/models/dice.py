import random

def rolar_3d6():
    return sum(random.randint(1,6) for _ in range(3))

def rolar_4d6_drop_lowest():
    rolls = [random.randint(1,6) for _ in range(4)]
    rolls.remove(min(rolls))
    return sum(rolls)

def gerar_atributos(modo):
    atributos = ["Força","Destreza","Constituição","Inteligência","Sabedoria","Carisma"]
    if modo == "3d6":
        valores = [rolar_3d6() for _ in range(6)]
        return dict(zip(atributos, valores))

    elif modo == "choose_values":
        valores = [rolar_3d6() for _ in range(6)]
        return valores

    elif modo == "4d6_drop_lowest":
        valores = [rolar_4d6_drop_lowest() for _ in range(6)]
        return valores