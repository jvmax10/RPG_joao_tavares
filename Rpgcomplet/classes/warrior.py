from .classe import Classe

class Warrior(Classe):
    def __init__(self):
        super().__init__("Guerreiro", "1d10")
        self.habilidades = ["Ataque Extra", "Uso de Armaduras Pesadas"]
