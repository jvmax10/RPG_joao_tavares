import random

# Classe para lidar com rolagens de dados
class Dice:
    @staticmethod
    def roll_dice(num, sides):
        """Rola 'num' dados de 'sides' lados e retorna a soma"""
        return sum(random.randint(1, sides) for _ in range(num))

    @staticmethod
    def roll_3d6():
        return Dice.roll_dice(3, 6)

    @staticmethod
    def roll_4d6_drop_lowest():
        rolls = [random.randint(1, 6) for _ in range(4)]
        rolls.remove(min(rolls))  # remove o menor dado
        return sum(rolls)


# Classe do Personagem
class Character:
    def __init__(self, name):
        self.name = name
        self.attributes = {
            "Força": 0,
            "Destreza": 0,
            "Constituição": 0,
            "Inteligência": 0,
            "Sabedoria": 0,
            "Carisma": 0
        }

    def set_attributes(self, values):
        for key, value in zip(self.attributes.keys(), values):
            self.attributes[key] = value

    def show_attributes(self):
        print(f"\nAtributos de {self.name}:")
        for attr, value in self.attributes.items():
            print(f"{attr}: {value}")


# Classe para gerar atributos nos três estilos
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


# Classe principal de interação
class Game:
    def main(self):
        print("=== Gerador de Atributos de Personagem ===")
        nome = input("Digite o nome do personagem: ")
        personagem = Character(nome)

        print("\nEscolha o estilo de geração de atributos:")
        print("1 - Estilo Clássico")
        print("2 - Estilo Aventureiro")
        print("3 - Estilo Heróico")
        escolha = input("Opção: ")

        if escolha == "1":
            atributos = AttributeGenerator.estilo_classico()
            personagem.set_attributes(atributos)

        elif escolha == "2":
            atributos = AttributeGenerator.estilo_aventureiro()
            personagem.set_attributes(atributos)

        elif escolha == "3":
            atributos = AttributeGenerator.estilo_heroico()
            personagem.set_attributes(atributos)

        else:
            print("Opção inválida. Saindo...")
            return

        personagem.show_attributes()


if __name__ == "__main__":
    Game().main()
