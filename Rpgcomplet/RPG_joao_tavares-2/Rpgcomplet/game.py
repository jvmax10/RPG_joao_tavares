from models.attributes import AttributeGenerator
from models.character import Character
from models.races.human import Human
from models.races.elf import Elf
from models.races.anao import Anao
from models.classes.warrior import Warrior
from models.classes.mage import Mage
from models.classes.rogue import Rogue

class Game:
    def main(self):
        print("=== CRIAÇÃO DE PERSONAGEM RPG ===")
        nome = input("Digite o nome do personagem: ")
        personagem = Character(nome)

        # Passo 1 - Atributos
        print("\nEscolha o estilo de geração de atributos:")
        print("1 - Estilo Clássico (3d6 na ordem)")
        print("2 - Estilo Aventureiro (3d6 e distribui)")
        print("3 - Estilo Heróico (4d6 drop lowest e distribui)")
        escolha = input("Opção: ")

        if escolha == "1":
            atributos = AttributeGenerator.estilo_classico()
        elif escolha == "2":
            atributos = AttributeGenerator.estilo_aventureiro()
        elif escolha == "3":
            atributos = AttributeGenerator.estilo_heroico()
        else:
            print("Opção inválida. Saindo...")
            return
        personagem.set_attributes(atributos)

        # Passo 2 - Escolher raça
        print("\nEscolha a raça do personagem:")
        racas = ["Humano", "Elfo", "Anão"]
        for i, r in enumerate(racas, start=1):
            print(f"{i} - {r}")
        r_escolha = int(input("Opção: "))
        if 1 <= r_escolha <= len(racas):
            personagem.choose_race(racas[r_escolha-1])
        else:
            print("Raça inválida.")

        # Passo 3 - Escolher classe
        print("\nEscolha a classe do personagem:")
        classes = ["Guerreiro", "Mago", "Ladino"]
        for i, c in enumerate(classes, start=1):
            print(f"{i} - {c}")
        c_escolha = int(input("Opção: "))
        if 1 <= c_escolha <= len(classes):
            personagem.choose_class(classes[c_escolha-1])
        else:
            print("Classe inválida.")

        # Mostrar ficha final

        personagem.show_character()
