from dice import Dice

class AttributeGenerator:
    @staticmethod
    def estilo_classico():
        """Rola 3d6 para cada atributo na ordem fixa"""
        return [Dice.roll_3d6() for _ in range(6)]

    @staticmethod
    def estilo_aventureiro():
        """Rola 3d6 seis vezes e o jogador distribui como quiser"""
        rolls = [Dice.roll_3d6() for _ in range(6)]
        print("\nResultados rolados:", rolls)
        valores = []
        for attr in ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]:
            escolha = int(input(f"Escolha um valor para {attr} a partir de {rolls}: "))
            while escolha not in rolls:
                escolha = int(input("Valor inválido. Escolha novamente: "))
            valores.append(escolha)
            rolls.remove(escolha)
        return valores

    @staticmethod
    def estilo_heroico():
        """Rola 4d6 drop lowest seis vezes e distribui como quiser"""
        rolls = [Dice.roll_4d6_drop_lowest() for _ in range(6)]
        print("\nResultados rolados:", rolls)
        valores = []
        for attr in ["Força", "Destreza", "Constituição", "Inteligência", "Sabedoria", "Carisma"]:
            escolha = int(input(f"Escolha um valor para {attr} a partir de {rolls}: "))
            while escolha not in rolls:
                escolha = int(input("Valor inválido. Escolha novamente: "))
            valores.append(escolha)
            rolls.remove(escolha)
        return valores
