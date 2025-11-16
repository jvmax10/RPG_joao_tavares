import json
import os

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
        self.race = None
        self.char_class = None

    def set_attributes(self, values):
        for key, value in zip(self.attributes.keys(), values):
            self.attributes[key] = value

    def choose_race(self, race):
        self.race = race
        print(f"{self.name} escolheu a raça {race}!")

    def choose_class(self, char_class):
        self.char_class = char_class
        print(f"{self.name} escolheu a classe {char_class}!")

    def show_character(self):
        print(f"\n=== FICHA DO PERSONAGEM ===")
        print(f"Nome: {self.name}")
        print(f"Raça: {self.race if self.race else 'Não definida'}")
        print(f"Classe: {self.char_class if self.char_class else 'Não definida'}")
        print("Atributos:")
        for attr, value in self.attributes.items():
            print(f"{attr}: {value}")

    # 🔥 MÉTODO NOVO: SALVAR PERSONAGEM EM JSON
    def save_to_json(self):
        dados = {
            "nome": self.name,
            "raca": self.race,
            "classe": self.char_class,
            "atributos": self.attributes
        }

        if not os.path.exists("personagens"):
            os.makedirs("personagens")

        caminho = f"personagens/{self.name}.json"

        with open(caminho, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

        print(f"\n✔️ Personagem salvo em: {caminho}")

